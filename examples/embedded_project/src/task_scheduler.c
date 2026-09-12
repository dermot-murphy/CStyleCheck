/**
 * @file task_scheduler.c
 * @brief Cooperative round-robin task scheduler implementation.
 *
 * Tasks are stored in a static array. task_scheduler_run() iterates the
 * array once per call and dispatches any task whose period has elapsed.
 * Execution order is deterministic: tasks are called in registration order.
 *
 * @copyright Copyright (c) 2026 EmbeddedDemo Project. All rights reserved.
 */

#include "task_scheduler.h"

/* --------------------------------------------------------------------------
 * Module state
 * -------------------------------------------------------------------------- */

static task_t  g_tasks[TASK_MAX_COUNT];
static uint8_t g_task_count = 0U;

/* --------------------------------------------------------------------------
 * Public functions
 * -------------------------------------------------------------------------- */

bool task_scheduler_add(task_fn_t fn, uint32_t interval_ms,
                        const char *p_name)
{
    if ((NULL == fn) || (TASK_MAX_COUNT <= g_task_count)) {
        return false;
    }
    if (0U == interval_ms) {
        return false;
    }

    task_t *p_task      = &g_tasks[g_task_count];
    p_task->fn          = fn;
    p_task->interval_ms = interval_ms;
    p_task->last_run_ms = 0U;
    p_task->enabled     = true;
    p_task->p_name      = p_name;

    g_task_count++;
    return true;
}

void task_scheduler_run(uint32_t now_ms)
{
    uint8_t i;
    for (i = 0U; i < g_task_count; i++) {
        task_t *p_task = &g_tasks[i];

        if (!p_task->enabled) {
            continue;
        }
        if ((now_ms - p_task->last_run_ms) >= p_task->interval_ms) {
            p_task->fn(now_ms);
            p_task->last_run_ms = now_ms;
        }
    }
}

void task_scheduler_enable(task_fn_t fn, bool enabled)
{
    uint8_t i;
    if (NULL == fn) {
        return;
    }
    for (i = 0U; i < g_task_count; i++) {
        if (g_tasks[i].fn == fn) {
            g_tasks[i].enabled = enabled;
            break;
        }
    }
}
