/**
 * @file task_scheduler.h
 * @brief Cooperative round-robin task scheduler.
 *
 * Tasks are registered with a period and are called by task_scheduler_run()
 * whenever their period has elapsed. All tasks share the same execution
 * context (no preemption) so individual task handlers must be non-blocking.
 *
 * @copyright Copyright (c) 2026 EmbeddedDemo Project. All rights reserved.
 */

#ifndef TASK_SCHEDULER_H
#define TASK_SCHEDULER_H

#include "project_config.h"

/* --------------------------------------------------------------------------
 * Types
 * -------------------------------------------------------------------------- */

/** Signature for a schedulable task callback. */
typedef void (*task_fn_t)(uint32_t now_ms);

/** Internal task descriptor - populated by task_scheduler_add(). */
typedef struct {
    task_fn_t   fn;           /**< Task entry-point function.        */
    uint32_t    interval_ms;  /**< Execution period in milliseconds. */
    uint32_t    last_run_ms;  /**< Tick at which task last executed. */
    bool        enabled;      /**< When false the task is skipped.  */
    const char *p_name;       /**< Human-readable name (debug use). */
} task_t;

/* --------------------------------------------------------------------------
 * Public API
 * -------------------------------------------------------------------------- */

/**
 * @brief Register a new task with the scheduler.
 * @param fn           Task callback; must not be NULL.
 * @param interval_ms  How often the task should run (> 0).
 * @param p_name       Descriptive name string (stored by pointer, not copied).
 * @return true on success, false if the task table is full or fn is NULL.
 */
bool task_scheduler_add(task_fn_t fn, uint32_t interval_ms,
                        const char *p_name);

/**
 * @brief Dispatch tasks whose period has elapsed.
 * @param now_ms  Current system tick in milliseconds.
 *
 * Call this from the main loop. Tasks are visited in registration order;
 * each enabled task is called at most once per invocation.
 */
void task_scheduler_run(uint32_t now_ms);

/**
 * @brief Enable or disable a previously registered task.
 * @param fn       The task function to update (used as a key).
 * @param enabled  true to enable, false to suspend.
 *
 * If fn was never registered this call is silently ignored.
 */
void task_scheduler_enable(task_fn_t fn, bool enabled);

#endif /* TASK_SCHEDULER_H */
