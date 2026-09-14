/**
 * @file led_control.h
 * @brief LED control public interface.
 *
 * Supports four modes: solid off, solid on, symmetric blink, and a
 * slow-pulse (ramp up / ramp down) pattern. All timing is driven by
 * the caller supplying the current tick in led_control_tick().
 *
 * @copyright Copyright (c) 2026 EmbeddedDemo Project. All rights reserved.
 */

#ifndef LED_CONTROL_H
#define LED_CONTROL_H

#include "project_config.h"

/* --------------------------------------------------------------------------
 * Types
 * -------------------------------------------------------------------------- */

/** Logical LED identifiers. */
typedef enum {
    LED_ID_STATUS = 0U,   /**< Green status indicator. */
    LED_ID_ERROR  = 1U,   /**< Red error indicator.    */
    LED_ID_COUNT          /**< Sentinel - do not use as an LED id. */
} led_id_t;

/** LED operating mode. */
typedef enum {
    LED_MODE_OFF   = 0U,  /**< Forced off.                                */
    LED_MODE_ON    = 1U,  /**< Forced on.                                 */
    LED_MODE_BLINK = 2U,  /**< Toggle at period_ms / 2 interval.         */
    LED_MODE_PULSE = 3U,  /**< Ramp on then ramp off over period_ms.     */
} led_mode_t;

/* --------------------------------------------------------------------------
 * Public API
 * -------------------------------------------------------------------------- */

/**
 * @brief Initialise the LED control module.
 *
 * Must be called once before any other led_control_* function.
 * Sets all LEDs to LED_MODE_OFF.
 */
void led_control_init(void);

/**
 * @brief Set the operating mode for one LED.
 * @param id         The LED to configure (must be < LED_ID_COUNT).
 * @param mode       The desired operating mode.
 * @param period_ms  Period in milliseconds; ignored for MODE_OFF / MODE_ON.
 */
void led_control_set_mode(led_id_t id, led_mode_t mode, uint16_t period_ms);

/**
 * @brief Advance LED animations by one tick.
 * @param now_ms  Current system tick in milliseconds.
 *
 * Call this function at a regular interval (e.g. from a 1 ms SysTick ISR
 * or from the main loop) to keep blink/pulse patterns running smoothly.
 */
void led_control_tick(uint32_t now_ms);

/**
 * @brief Return the current logical state of one LED.
 * @param id  LED to query (must be < LED_ID_COUNT).
 * @return    true when the LED is logically on, false otherwise.
 */
bool led_control_is_on(led_id_t id);

#endif /* LED_CONTROL_H */
