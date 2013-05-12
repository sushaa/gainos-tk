
/* Copyright(C) 2013, GaInOS-TK by Fan Wang. All rights reserved.
 * Generated by GaInOS-TK Studio at 2013-05-12:15-57-00. 
 * Don't Modify it by hand.
 */
#ifndef _OSEK_CFG_H_
#define _OSEK_CFG_H_
/* =====================  MISC  ========================== */
#define cfgOS_STATUS_LEVEL OS_STATUS_STANDARD
#define CHIP_STM32F1
//#define CHIP_MC9S12
#if defined(CHIP_MC9S12) //9s12
#define CPU_FREQUENCY        32000000 /* HZ */
#define OSC_FREQUENCY         8000000 /* HZ */
#elif defined(CHIP_STM32F1)//stm32
#define CPU_FREQUENCY        72000000 /* HZ */
#elif defined(CHIP_AT91SAM3S)
#define CPU_FREQUENCY        64000000 /* HZ */
#elif defined(CHIP_MPC56XX)
#define CPU_FREQUENCY  64000000   /* HZ */
#define OSC_FREQUENCY  8000000    /* Oscillator Clock 8MHZ */
#endif

/* =====================  TASK  ========================== */
#define cfgOSEK_MAX_PRIO 10
#define cfgOSEK_TASK_NUM  5
#define ID_vTaskInit 0
#define ID_vTaskSender 1
#define ID_vTaskReceiver 2
#define ID_vTaskMainFunction 3
#define ID_vTaskIdle 4
IMPORT TASK(vTaskInit);
IMPORT TASK(vTaskSender);
IMPORT TASK(vTaskReceiver);
IMPORT TASK(vTaskMainFunction);
IMPORT TASK(vTaskIdle);

/* =====================  EVENT ========================== */
#define ID_vTaskReceiverEvent 0
#define vTaskReceiverCanRxEvent 0x1
#define cfgOSEK_EVENTFLAG_NUM 1

/* =====================  ALARM ========================== */
#define cfgOSEK_COUNTER_NUM 1
#define ID_vSystemCounter 0
#define cfgOSEK_ALARM_NUM 3
#define ID_vAlarmSender 0
IMPORT ALARM(vAlarmSender);
#define ID_vAlarmReceiver 1
IMPORT ALARM(vAlarmReceiver);
#define ID_vAlarmMainFunction 2
IMPORT ALARM(vAlarmMainFunction);

/*  ====================  RESOURCE ======================= */
#define cfgOSEK_RESOURCE_NUM 1
#define ID_RES_SCHEDULER 0

/*  ====================  HOOKs    ======================= */
#define cfgOS_SHUT_DOWN_HOOK 0
#define cfgOS_START_UP_HOOK  0
#endif /* _OSEK_CFG_H_ */
