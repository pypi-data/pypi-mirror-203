#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-2.0

"""
Contains core functions for DAMON sysfs control.
"""

import os
import time

import _damo_fs
import _damon

feature_supports = None

# Use only one kdamond, one context, and one target for now
root_dir = '/sys/kernel/mm/damon'
admin_dir = os.path.join(root_dir, 'admin')
kdamonds_dir = os.path.join(admin_dir, 'kdamonds')
nr_kdamonds_file = os.path.join(kdamonds_dir, 'nr_kdamonds')

def kdamond_dir_of(kdamond_name):
    return os.path.join(admin_dir, 'kdamonds', '%s' % kdamond_name)

def state_file_of(kdamond_name):
    return os.path.join(kdamond_dir_of(kdamond_name), 'state')

def ctx_dir_of(kdamond_name, context_name):
    return os.path.join(
            kdamond_dir_of(kdamond_name), 'contexts', '%s' % context_name)

def schemes_dir_of(kdamond_name, context_name):
    return os.path.join(ctx_dir_of(kdamond_name, context_name), 'schemes')

def scheme_dir_of(kdamond_name, context_name, scheme_name):
    return os.path.join(
            schemes_dir_of(kdamond_name, context_name), '%s' % scheme_name)

def scheme_tried_regions_dir_of(kdamond_name, context_name, scheme_name):
    return os.path.join(
            scheme_dir_of(kdamond_name, context_name, scheme_name),
            'tried_regions')

def supported():
    return os.path.isdir(kdamonds_dir)

def turn_damon_on(kdamonds_names):
    # In case of vaddr, too early monitoring shows unstable mapping changes.
    # Give the process a time to have stable memory mapping.
    time.sleep(0.5)
    for kdamond_name in kdamonds_names:
        err = _damo_fs.write_file(state_file_of(kdamond_name), 'on')
        if err != None:
            return err
    return None

def turn_damon_off(kdamonds_names):
    for kdamond_name in kdamonds_names:
        err = _damo_fs.write_file(state_file_of(kdamond_name), 'off')
        if err != None:
            return err
    return None

def is_kdamond_running(kdamond_name):
    content, err = _damo_fs.read_file(state_file_of(kdamond_name))
    if err != None:
        print(err)
        return False
    return content.strip() == 'on'

'Return error'
def update_schemes_stats(kdamond_names):
    for kdamond_name in kdamond_names:
        err = _damo_fs.write_file(
                state_file_of(kdamond_name), 'update_schemes_stats')
        if err != None:
            return err
    return None

'Return error'
def update_schemes_tried_regions(kdamond_names):
    for kdamond_name in kdamond_names:
        err = _damo_fs.write_file(
                state_file_of(kdamond_name), 'update_schemes_tried_regions')
        if err != None:
            return err
    return None

# for stage_kdamonds

def wops_for_scheme_filter(damos_filter):
    return {
        'type': '%s' % damos_filter.filter_type,
        'memcg_path': ('%s' % damos_filter.memcg_path
            if damos_filter.memcg_path != None else ''),
        'matching': 'Y' if damos_filter.matching else 'N',
        }

def wops_for_scheme_filters(filters):
    wops = {}
    for idx, damos_filter in enumerate(filters):
        wops['%d' % idx] = wops_for_scheme_filter(damos_filter)
    return wops

def wops_for_scheme_watermarks(wmarks):
    if wmarks == None:
        return {}
    return {
        'metric': wmarks.metric,
        'interval_us': '%d' % wmarks.interval_us,
        'high': '%d' % wmarks.high_permil,
        'mid': '%d' % wmarks.mid_permil,
        'low': '%d' % wmarks.low_permil,
    }

def wops_for_scheme_quotas(quotas):
    if quotas == None:
        return {}
    return {
        'ms': '%d' % quotas.time_ms,
        'bytes': '%d' % quotas.sz_bytes,
        'reset_interval_ms': '%d' % quotas.reset_interval_ms,
        'weights': {
            'sz_permil': '%d' % quotas.weight_sz_permil,
            'nr_accesses_permil': '%d' % quotas.weight_nr_accesses_permil,
            'age_permil': '%d' % quotas.weight_age_permil,
        },
    }

def wops_for_scheme_access_pattern(pattern, ctx):
    if pattern == None:
        return {}
    pattern = pattern.converted_for_units(
            _damon.unit_sample_intervals, _damon.unit_aggr_intervals,
            ctx.intervals)

    return {
        'sz': {
            'min': '%d' % pattern.sz_bytes[0],
            'max': '%d' % pattern.sz_bytes[1],
        },
        'nr_accesses': {
            'min': '%d' % pattern.nr_accesses[0].value,
            'max': '%d' % pattern.nr_accesses[1].value,
        },
        'age': {
            'min': '%d' % pattern.age[0].value,
            'max': '%d' % pattern.age[1].value,
        },
    }

def wops_for_schemes(ctx):
    schemes = ctx.schemes

    schemes_wops = {}
    for idx, scheme in enumerate(schemes):
        scheme_dir_name = '%d' % idx
        schemes_wops[scheme_dir_name] = {
            'access_pattern': wops_for_scheme_access_pattern(
                scheme.access_pattern, ctx),
            'action': scheme.action,
            'quotas': wops_for_scheme_quotas(scheme.quotas),
            'watermarks': wops_for_scheme_watermarks(scheme.watermarks),
        }
        if feature_supported('schemes_filters'):
            schemes_wops[scheme_dir_name]['filters'] = wops_for_scheme_filters(
                    scheme.filters)
    return schemes_wops

def wops_for_regions(regions):
    return {'%d' % region_idx: {
        'start': '%d' % region.start,
        'end': '%d' % region.end}
        for region_idx, region in enumerate(regions)}

def wops_for_targets(ctx):
    return {
            '%d' % idx: {
                'pid_target': '%s' %
                target.pid if _damon.target_has_pid(ctx.ops) else '',
                'regions': wops_for_regions(target.regions)
                } for idx, target in enumerate(ctx.targets)}

def wops_for_monitoring_attrs(ctx):
    return {
        'intervals': {
            'sample_us': '%d' % ctx.intervals.sample,
            'aggr_us': '%d' % ctx.intervals.aggr,
            'update_us': '%d' % ctx.intervals.ops_update,
        },
        'nr_regions': {
            'min': '%d' % ctx.nr_regions.minimum,
            'max': '%d' % ctx.nr_regions.maximum,
        },
    }

def wops_for_ctx(ctx):
    ops = ctx.ops
    if ops == 'fvaddr' and not feature_supported('fvaddr'):
        ops = 'vaddr'
    return [
            {'operations': ops},
            {'monitoring_attrs': wops_for_monitoring_attrs(ctx)},
            {'targets': wops_for_targets(ctx)},
            {'schemes': wops_for_schemes(ctx)},
    ]

def wops_for_ctxs(ctxs):
    return {'%d' % idx: wops_for_ctx(ctx) for idx, ctx in enumerate(ctxs)}

def wops_for_kdamond(kdamond):
    return {'contexts': wops_for_ctxs(kdamond.contexts)}

def wops_for_kdamonds(kdamonds):
    return {'%d' % idx: wops_for_kdamond(kdamond)
            for idx, kdamond in enumerate(kdamonds)}

def __ensure_scheme_dir_populated(scheme_dir, scheme):
    if not feature_supported('schemes_filters'):
        return

    nr_filters_path = os.path.join(scheme_dir, 'filters', 'nr_filters')

    nr_filters, err = _damo_fs.read_file(nr_filters_path)
    if err != None:
        raise Exception('nr_filters read fail (%s)' % err)
    if int(nr_filters) != len(scheme.filters):
        _damo_fs.write_file(nr_filters_path, '%d' % len(scheme.filters))

def __ensure_target_dir_populated(target_dir, target):
    nr_regions_path = os.path.join(target_dir, 'regions', 'nr_regions')
    nr_regions, err = _damo_fs.read_file(nr_regions_path)
    if err != None:
        raise Exception('nr_regions read fail (%s)' % err)
    if int(nr_regions) != len(target.regions):
        _damo_fs.write_file(nr_regions_path, '%d' % len(target.regions))

def __ensure_kdamond_dir_populated(kdamond_dir, kdamond):
    contexts_dir_path = os.path.join(kdamond_dir, 'contexts')
    nr_contexts_path = os.path.join(kdamond_dir, 'contexts', 'nr_contexts')
    nr_contexts, err = _damo_fs.read_file(nr_contexts_path)
    if err != None:
        raise Exception('kdamond name read fail (%s)' % err)
    if int(nr_contexts) != len(kdamond.contexts):
        _damo_fs.write_file(nr_contexts_path, '%d' % len(kdamond.contexts))

    for ctx_idx, ctx in enumerate(kdamond.contexts):
        ctx_dir_path = os.path.join(contexts_dir_path, '%d' % ctx_idx)
        targets_dir_path = os.path.join(ctx_dir_path, 'targets')
        nr_targets_path = os.path.join(targets_dir_path, 'nr_targets')
        nr_targets, err = _damo_fs.read_file(nr_targets_path)
        if err != None:
            raise Exception('nr_targets read fail (%s)' % err)
        if int(nr_targets) != len(ctx.targets):
            _damo_fs.write_file(nr_targets_path, '%d' % len(ctx.targets))

        for target_idx, target in enumerate(ctx.targets):
            target_dir_path = os.path.join(targets_dir_path, '%d' % target_idx)
            __ensure_target_dir_populated(target_dir_path, target)

        schemes_dir_path = os.path.join(ctx_dir_path, 'schemes')
        nr_schemes_path = os.path.join(schemes_dir_path, 'nr_schemes')
        nr_schemes, err = _damo_fs.read_file(nr_schemes_path)
        if err != None:
            raise Exception('nr_schemes read fail (%s)' % err)
        if int(nr_schemes) != len(ctx.schemes):
            _damo_fs.write_file(nr_schemes_path, '%d' % len(ctx.schemes))

        for scheme_idx, scheme in enumerate(ctx.schemes):
            scheme_dir_path = os.path.join(schemes_dir_path, '%d' % scheme_idx)
            __ensure_scheme_dir_populated(scheme_dir_path, scheme)

def __ensure_dirs_populated_for(kdamonds):
    nr_kdamonds, err = _damo_fs.read_file(nr_kdamonds_file)
    if err != None:
        raise Exception('nr_kdamonds_file read fail (%s)' % err)
    if int(nr_kdamonds) != len(kdamonds):
        _damo_fs.write_file(nr_kdamonds_file, '%d' % len(kdamonds))
    for idx, kdamond in enumerate(kdamonds):
        kdamond_dir = kdamond_dir_of('%d' % idx)
        __ensure_kdamond_dir_populated(kdamond_dir, kdamond)

def ensure_dirs_populated_for(kdamonds):
    try:
        __ensure_dirs_populated_for(kdamonds)
    except Exception as e:
        print('sysfs dirs population failed (%s)' % e)
        exit(1)

def stage_kdamonds(kdamonds):
    if len(kdamonds) > 1:
        return 'currently only <=one kdamond is supported'
    if len(kdamonds) == 1 and len(kdamonds[0].contexts) > 1:
        return 'currently only <=one damon_ctx is supported'
    if (len(kdamonds) == 1 and len(kdamonds[0].contexts) == 1 and
            len(kdamonds[0].contexts[0].targets) > 1):
        return 'currently only <=one target is supported'
    ensure_dirs_populated_for(kdamonds)

    return _damo_fs.write_files({kdamonds_dir: wops_for_kdamonds(kdamonds)})

# for current_kdamonds()

def files_content_to_access_pattern(files_content):
    return _damon.DamosAccessPattern(
            [int(files_content['sz']['min']),
                int(files_content['sz']['max'])],
            [int(files_content['nr_accesses']['min']),
                int(files_content['nr_accesses']['max'])],
            _damon.unit_sample_intervals, # nr_accesses_unit
            [int(files_content['age']['min']),
                int(files_content['age']['max'])],
            _damon.unit_aggr_intervals) # age_unit

def files_content_to_quotas(files_content):
    return _damon.DamosQuotas(
            int(files_content['ms']),
            int(files_content['bytes']),
            int(files_content['reset_interval_ms']),
            [int(files_content['weights']['sz_permil']),
                int(files_content['weights']['nr_accesses_permil']),
                int(files_content['weights']['age_permil'])])

def files_content_to_watermarks(files_content):
    return _damon.DamosWatermarks(
            files_content['metric'].strip(),
            int(files_content['interval_us']),
            int(files_content['high']),
            int(files_content['mid']),
            int(files_content['low']))

def files_content_to_damos_filters(files_content):
    filters = []
    for filter_dir_name in files_content:
        if filter_dir_name == 'nr_filters':
            continue
        filter_kv = files_content[filter_dir_name]
        filters.append(_damon.DamosFilter(filter_kv['type'].strip(),
            filter_kv['memcg_path'].strip(), filter_kv['matching'].strip()))
    return filters

def files_content_to_damos_stats(files_content):
    return _damon.DamosStats(
            int(files_content['nr_tried']),
            int(files_content['sz_tried']),
            int(files_content['nr_applied']),
            int(files_content['sz_applied']),
            int(files_content['qt_exceeds']))

def files_content_to_damos_tried_regions(files_content):
    regions = []
    nr_region_dirs = len(files_content)
    if 'sz_regions_sum' in files_content:
        nr_region_dirs -= 1
    for i in range(nr_region_dirs):
        regions.append(_damon.DamosTriedRegion(
            int(files_content['%d' % i]['start']),
            int(files_content['%d' % i]['end']),
            int(files_content['%d' % i]['nr_accesses']),
            int(files_content['%d' % i]['age']),
            _damon.unit_aggr_intervals
            ))
    return regions

def files_content_to_scheme(files_content):
    return _damon.Damos(
            files_content_to_access_pattern(files_content['access_pattern']),
            files_content['action'].strip(),
            files_content_to_quotas(files_content['quotas']),
            files_content_to_watermarks(files_content['watermarks']),
            files_content_to_damos_filters(files_content['filters'])
                if 'filters' in files_content else [],
            files_content_to_damos_stats(files_content['stats']),
            files_content_to_damos_tried_regions(
                files_content['tried_regions'])
                if 'tried_regions' in files_content else [])

def files_content_to_regions(files_content):
    regions = []
    for region_idx in range(int(files_content['nr_regions'])):
        region_name = '%d' % region_idx
        regions.append(_damon.DamonRegion(
            int(files_content[region_name]['start']),
            int(files_content[region_name]['end'])))
    return regions

def files_content_to_target(files_content):
    try:
        pid = int(files_content['pid_target'])
    except:
        pid = None
    regions = files_content_to_regions(files_content['regions'])
    return _damon.DamonTarget(pid, regions)

def files_content_to_context(context_name, files_content):
    mon_attrs_content = files_content['monitoring_attrs']
    intervals_content = mon_attrs_content['intervals']
    intervals = _damon.DamonIntervals(
            int(intervals_content['sample_us']),
            int(intervals_content['aggr_us']),
            int(intervals_content['update_us']))
    nr_regions_content = mon_attrs_content['nr_regions']
    nr_regions = _damon.DamonNrRegionsRange(
            int(nr_regions_content['min']),
            int(nr_regions_content['max']))
    ops = files_content['operations'].strip()

    targets_content = files_content['targets']
    targets = []
    for target_dir_name, target_content in targets_content.items():
        if target_dir_name == 'nr_targets':
            continue
        targets.append(files_content_to_target(target_content))

    schemes_content = files_content['schemes']
    schemes = []
    for scheme_name, scheme_content in schemes_content.items():
        if scheme_name == 'nr_schemes':
            continue
        schemes.append(files_content_to_scheme(scheme_content))

    return _damon.DamonCtx(intervals, nr_regions, ops, targets, schemes)

def files_content_to_kdamond(files_content):
    contexts_content = files_content['contexts']
    contexts = []
    for ctx_name in contexts_content:
        if ctx_name == 'nr_contexts':
            continue
        contexts.append(files_content_to_context(ctx_name,
            contexts_content[ctx_name]))
    state = files_content['state'].strip()
    pid = files_content['pid'].strip()
    return _damon.Kdamond(state, pid, contexts)

def files_content_to_kdamonds(files_contents):
    kdamonds = []
    for kdamond_name in files_contents:
        if kdamond_name == 'nr_kdamonds':
            continue
        kdamonds.append(files_content_to_kdamond(files_contents[kdamond_name]))
    return kdamonds

def current_kdamonds():
    return files_content_to_kdamonds(
            _damo_fs.read_files(kdamonds_dir))

def current_kdamond_names():
    # TODO: Do not read recursive but just one depth
    return [x for x in _damo_fs.read_files(kdamonds_dir).keys()
            if x != 'nr_kdamonds']

def commit_staged(kdamond_names):
    for kdamond_name in kdamond_names:
        err = _damo_fs.write_file(state_file_of(kdamond_name), 'commit')
        if err != None:
            return err
    return None

# features

def feature_supported(feature):
    if feature_supports == None:
        update_supported_features()
    return feature_supports[feature]

features_sysfs_support_from_begining = [
        'schemes',
        'init_regions',
        'vaddr',
        'fvaddr',
        'paddr',
        'init_regions_target_idx',
        'schemes_speed_limit',
        'schemes_quotas',
        'schemes_prioritization',
        'schemes_wmarks',
        'schemes_stat_succ',
        'schemes_stat_qt_exceed',
        ]

def _avail_ops():
    '''Assumes called by update_supported_features() assuming one scheme.
    Returns available ops input and error'''
    avail_ops = []
    avail_operations_filepath = os.path.join(ctx_dir_of(0, 0),
            'avail_operations')
    if not os.path.isfile(avail_operations_filepath):
        operations_filepath = os.path.join(ctx_dir_of(0, 0), 'operations')
        for ops in ['vaddr', 'paddr', 'fvaddr']:
            err = _damo_fs.write_file(operations_filepath, ops)
            if err != None:
                avail_ops.append(ops)
        return avail_ops, None

    content, err = _damo_fs.read_file(avail_operations_filepath)
    if err != None:
        return None, err
    return content.strip().split(), None

def update_supported_features():
    global feature_supports

    if feature_supports != None:
        return None
    feature_supports = {x: False for x in _damon.features}

    if not supported():
        return 'damon sysfs dir (%s) not found' % kdamonds_dir
    for feature in features_sysfs_support_from_begining:
        feature_supports[feature] = True

    orig_kdamonds = None
    if not os.path.isdir(scheme_dir_of(0, 0, 0)):
        orig_kdamonds = current_kdamonds()
        kdamonds_for_feature_check = [_damon.Kdamond(state=None,
            pid=None, contexts=[_damon.DamonCtx(intervals=None,
                nr_regions=None, ops=None, targets=[],
                schemes=[_damon.Damos(access_pattern=None,
                    action='stat', quotas=None, watermarks=None, filters=[],
                    stats=None)])])]
        ensure_dirs_populated_for(kdamonds_for_feature_check)

    if os.path.isdir(scheme_tried_regions_dir_of(0, 0, 0)):
        feature_supports['schemes_tried_regions'] = True

    if os.path.isfile(os.path.join(scheme_tried_regions_dir_of(0, 0, 0),
            'sz_regions_sum')):
        feature_supports['schemes_tried_regions_sz'] = True

    if os.path.isdir(os.path.join(scheme_dir_of(0, 0, 0), 'filters')):
        feature_supports['schemes_filters'] = True

    avail_ops, err = _avail_ops()
    if err == None:
        for ops in ['vaddr', 'paddr', 'fvaddr']:
            feature_supports[ops] = ops in avail_ops
    if orig_kdamonds != None:
        err = stage_kdamonds(orig_kdamonds)
    return err
