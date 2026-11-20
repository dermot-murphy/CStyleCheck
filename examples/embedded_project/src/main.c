/**
 * @file main.c
 * @brief Application entry point and top-level task configuration.
 *
 * Demonstrates how to wire the LED control and task scheduler modules
 * together in a typical cooperative embedded control loop. Replace the
 * sys_get_tick_ms() stub with your BSP hardware timer read.
 *
 * @copyright Copyright (c) 2026 EmbeddedDemo Project. All rights reserved.
 */

#include "led_control.h"
#include "task_scheduler.h"

/* --------------------------------------------------------------------------
 * Private function prototypes
 * -------------------------------------------------------------------------- */

static uint32_t sys_get_tick_ms(void);
static void     task_led_update(uint32_t now_ms);
static void     task_system_monitor(uint32_t now_ms);
static void     task_heartbeat(uint32_t now_ms);

/* --------------------------------------------------------------------------
 * Module state
 * -------------------------------------------------------------------------- */

/** Simulated millisecond counter. Replace with hardware timer read. */
static uint32_t g_tick_ms = 0U;

/** Heartbeat counter - incremented every heartbeat tick. */
static uint32_t g_heartbeat_count = 0U;

/* --------------------------------------------------------------------------
 * Application entry point
 * -------------------------------------------------------------------------- */

int main(void)
{
    /* Initialise modules */
    led_control_init();

    /* Configure LEDs */
    led_control_set_mode(LED_ID_STATUS, LED_MODE_BLINK, LED_DEFAULT_PERIOD_MS);
    led_control_set_mode(LED_ID_ERROR,  LED_MODE_OFF,   0U);

    /* Register tasks */
    (void)task_scheduler_add(task_led_update,      10U,   "led");
    (void)task_scheduler_add(task_heartbeat,       500U,  "heartbeat");
    (void)task_scheduler_add(task_system_monitor,  100U,  "monitor");

    /* Main loop */
    for (;;) {
        uint32_t now_ms = sys_get_tick_ms();
        task_scheduler_run(now_ms);
    }

    return 0; /* Unreachable - satisfies MISRA C:2012 Rule 16.3. */
}

/* --------------------------------------------------------------------------
 * Task callbacks
 * -------------------------------------------------------------------------- */

/**
 * @brief Drive LED animations forward by one scheduler tick.
 * @param now_ms  Current system tick in milliseconds.
 */
static void task_led_update(uint32_t now_ms)
{
    led_control_tick(now_ms);
}

/**
 * @brief System heartbeat - toggles error LED on fault detection.
 * @param now_ms  Current system tick in milliseconds.
 */
static void task_heartbeat(uint32_t now_ms)
{
    (void)now_ms;
    g_heartbeat_count++;

    /* Switch error LED to pulse mode on first heartbeat as a self-test. */
    if (1U == g_heartbeat_count) {
        led_control_set_mode(LED_ID_ERROR, LED_MODE_PULSE, 2000U);
    }
}

/**
 * @brief Monitor system health and set error LED on fault.
 * @param now_ms  Current system tick in milliseconds.
 */
static void task_system_monitor(uint32_t now_ms)
{
    /* Placeholder: read ADC channels, check thresholds, latch faults.
     * Example: if (adc_read(ADC_TEMP_CH) > TEMP_FAULT_THRESHOLD_ADC) {
     *              led_control_set_mode(LED_ID_ERROR, LED_MODE_BLINK, 200U);
     *          } */
    (void)now_ms;
}

/* --------------------------------------------------------------------------
 * Hardware abstraction stub
 * -------------------------------------------------------------------------- */

/**
 * @brief Return the current system tick in milliseconds.
 * @return Milliseconds since startup.
 *
 * In production replace this with a BSP call such as:
 *   return HAL_GetTick();   (STM32 HAL)
 *   return xTaskGetTickCount() * portTICK_PERIOD_MS;  (FreeRTOS)
 */
static uint32_t sys_get_tick_ms(void)
{
    g_tick_ms++;
    return g_tick_ms;
}
