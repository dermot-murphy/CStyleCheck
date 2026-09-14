/**
 * @file led_control.c
 * @brief LED control module implementation.
 *
 * Implements solid on/off, symmetric blink, and a linear pulse pattern.
 * Hardware write is abstracted behind led_hw_write() so the module can be
 * unit-tested without a real GPIO peripheral.
 *
 * @copyright Copyright (c) 2026 EmbeddedDemo Project. All rights reserved.
 */

#include "led_control.h"

/* --------------------------------------------------------------------------
 * Private types
 * -------------------------------------------------------------------------- */

/** Internal state for one physical LED. */
typedef struct {
    led_mode_t mode;           /**< Current operating mode.                */
    uint16_t   period_ms;      /**< Animation period (ms).                 */
    uint32_t   last_toggle_ms; /**< Last blink/pulse transition tick.      */
    uint8_t    pulse_step;     /**< Current pulse ramp position (0-100).   */
    bool       state;          /**< Logical output level (true = on).      */
} led_state_t;

/* --------------------------------------------------------------------------
 * Module state
 * -------------------------------------------------------------------------- */

static led_state_t g_led[LED_ID_COUNT];

/* --------------------------------------------------------------------------
 * Private helpers
 * -------------------------------------------------------------------------- */

/**
 * @brief Write the LED output to hardware (platform stub).
 * @param id   LED index.
 * @param on   Desired output level.
 */
static void led_hw_write(led_id_t id, bool on)
{
    /* Replace with GPIO register write or BSP call for your platform.
     * Example: HAL_GPIO_WritePin(LED_PORT, led_pins[id],
     *                            on ? GPIO_PIN_SET : GPIO_PIN_RESET); */
    (void)id;
    (void)on;
}

/**
 * @brief Update blink state for one LED.
 * @param p_led   Pointer to the LED state struct.
 * @param now_ms  Current tick.
 */
static void led_update_blink(led_state_t *p_led, uint32_t now_ms)
{
    uint32_t half_period = (uint32_t)p_led->period_ms / 2U;
    if ((now_ms - p_led->last_toggle_ms) >= half_period) {
        p_led->state           = !p_led->state;
        p_led->last_toggle_ms  = now_ms;
    }
}

/**
 * @brief Update pulse state for one LED.
 * @param p_led   Pointer to the LED state struct.
 * @param now_ms  Current tick.
 */
static void led_update_pulse(led_state_t *p_led, uint32_t now_ms)
{
    uint32_t step_ms = (uint32_t)p_led->period_ms / (2U * LED_PULSE_STEPS);
    if (step_ms < 1U) {
        step_ms = 1U;
    }
    if ((now_ms - p_led->last_toggle_ms) >= step_ms) {
        p_led->pulse_step      = (p_led->pulse_step + 1U) % (uint8_t)(2U * LED_PULSE_STEPS);
        p_led->state           = (p_led->pulse_step < LED_PULSE_STEPS);
        p_led->last_toggle_ms  = now_ms;
    }
}

/* --------------------------------------------------------------------------
 * Public functions
 * -------------------------------------------------------------------------- */

void led_control_init(void)
{
    uint8_t i;
    for (i = 0U; i < (uint8_t)LED_ID_COUNT; i++) {
        g_led[i].mode           = LED_MODE_OFF;
        g_led[i].period_ms      = 0U;
        g_led[i].last_toggle_ms = 0U;
        g_led[i].pulse_step     = 0U;
        g_led[i].state          = false;
        led_hw_write((led_id_t)i, false);
    }
}

void led_control_set_mode(led_id_t id, led_mode_t mode, uint16_t period_ms)
{
    if (LED_ID_COUNT <= (uint8_t)id) {
        return;
    }
    g_led[id].mode      = mode;
    g_led[id].period_ms = period_ms;
    g_led[id].state     = (LED_MODE_ON == mode);
    g_led[id].pulse_step = 0U;

    led_hw_write(id, g_led[id].state);
}

void led_control_tick(uint32_t now_ms)
{
    uint8_t i;
    for (i = 0U; i < (uint8_t)LED_ID_COUNT; i++) {
        led_state_t *p_led = &g_led[i];

        switch (p_led->mode) {
            case LED_MODE_BLINK:
                led_update_blink(p_led, now_ms);
                led_hw_write((led_id_t)i, p_led->state);
                break;

            case LED_MODE_PULSE:
                led_update_pulse(p_led, now_ms);
                led_hw_write((led_id_t)i, p_led->state);
                break;

            case LED_MODE_OFF:
            case LED_MODE_ON:
            default:
                /* Static modes - no animation update needed. */
                break;
        }
    }
}

bool led_control_is_on(led_id_t id)
{
    if (LED_ID_COUNT <= (uint8_t)id) {
        return false;
    }
    return g_led[id].state;
}
