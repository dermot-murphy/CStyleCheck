/**
 * @file project_config.h
 * @brief Project-wide constants, type aliases and compile-time configuration.
 *
 * Central header included by every module. Keep this file small; only put
 * definitions here that are genuinely needed across the whole project.
 *
 * @copyright Copyright (c) 2026 EmbeddedDemo Project. All rights reserved.
 */

#ifndef PROJECT_CONFIG_H
#define PROJECT_CONFIG_H

#include <stdint.h>
#include <stdbool.h>
#include <stddef.h>
#include <string.h>

/* System tick rate -------------------------------------------------------- */
/** System tick frequency in Hz (1 kHz = 1 ms resolution). */
#define SYS_TICK_HZ         1000U

/* Task scheduler ---------------------------------------------------------- */
/** Maximum number of tasks the scheduler can hold. */
#define TASK_MAX_COUNT      8U

/* LED control ------------------------------------------------------------- */
/** Default blink period when no period is specified (milliseconds). */
#define LED_DEFAULT_PERIOD_MS  500U

/** Number of PWM duty-cycle steps for PULSE mode. */
#define LED_PULSE_STEPS     100U

/* ADC -------------------------------------------------------------------- */
/** Number of ADC channels used by the application. */
#define ADC_CHANNEL_COUNT   4U

/** ADC full-scale value for a 12-bit converter. */
#define ADC_FULL_SCALE      4095U

#endif /* PROJECT_CONFIG_H */
