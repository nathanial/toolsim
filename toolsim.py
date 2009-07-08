
class Time(object):
    def __init__(self, year, month, day, hour, second):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.second = second

class Tool(object):

    def display_machine_time(self):
        """
        Syntax: T
        Function: Display the current machine time, "Year Month Day Hour Minute Second"         """
        pass

    def set_year(self, year):
        """
        Syntax: TY <Year>
        Function: set current year to "Year", which is the year number from 2000
        Input: Year >= 0
        E.G.: TY 7 --> set year to 2007
        """
        pass

    def set_month(self, month):
        """
        Syntax: TM <Month>
        Input: Month = 1-12
        """
        pass

    def set_day(self, day):
        """
        Syntax: TD <Day>
        Input: Day = 1-30
        """
        pass

    def set_hour(self, hour):
        """
        Syntax: TH <Hour>
        Input: Hour = 0-23
        """
        pass
    
    def set_minute(self, minute):
        """
        Syntax: TN <Minute>
        Input: Minute = 0-59
        """
        pass

    def set_second(self, second):
        """
        Syntax: TS <Second>
        Input: Second = 0-59
        """
        pass

    def set_data_log_rate(self, milliseconds):
        """
        Syntax: TR <# of ms>
        Function: Set the time to log the data to the flash, unit in ms
        E.G.: TR 3E8 --> log data every 1000ms
        """
        pass

    def set_quiet_mode_time_delay(self, milliseconds):
        """
        Syntax: TT <# of ms>
        Function: Set the time delay before switching to quiet mode, unit in ms
        E.G.: TT 493E0 --> switching to quiet mode after 5 mins
        """
        pass

    def set_data_send_duration(self, milliseconds):
        """
        Syntax: TF <# of ms>
        Function: Set the duration to send data acquired during quiet period, unit in ms
        E.G.: TF 927C0 --> send acquired quiet data for 10 mins
        """
        pass
    
    def read_logging_data(self):
        """
        Syntax: RL
        Function: Read logging data (0xD600-0x7FFFF) from memory, press "Esc" to terminate.
        """
        pass

    def read_logging_data_address(self):
        """
        Syntax: RLE
        Function: Read current logging data saving address
        """
        pass

    def read_calibration_constants(self):
        """
        Syntax: RC
        Function: Read calibration constants from the flash memory
        """
        pass
    
    def read_pulse_pattern_profile(self):
        """
        Syntax: RP
        Function: Read the pulse pattern profile.
        """
        pass

    def read_pulse_pattern_sequence_profile(self):
        """
        Syntax: RQ
        Function: Read the pule pattern sequence profile
        """
        pass

    def read_status_constant_profile(self):
        """
        Syntax: RT
        Function: Read the status constant profile, 
                  these constant determine how the tool functions.
        """
        pass

    def read_bytes_from_memory(self, address):
        """
        Syntax: RF <Address>
        Function: Read two bytes (16 bits) from flash memory starting at "Address"
        Input: Address = 0-80000
        E.G.: RF 7300 --> display "FFFF" last 32 bits -- logging time in milliseconds
        """
        pass

    def erase_flash_memory(self):
        """
        Syntax: WE
        Function: Write to erase the flash memory with "FFFF", make take a minute.
        """
        pass

    def set_calibration_constant(self, coeff, value):
        """
        Syntax: WC <Coeff> <Value>
        Function: Change the calibration constant indicated by "Coeff" with "Value"
        Input: Coeff = 0-13 (0-5 are accelerometer constant, 6-B are magnetometer constant) Value = 0-FFFF (C-D Temp Constant)
        E.G.: WC 0 1111 --> change the first constant (Gxmean) value to "1111"
        """
        pass

    def set_sms_constant_rotation(self, sensor, value):
        """
        Syntax: WR <Sensor> <Value>
        Function: Set the slow motion sensitivity constant of any of the 6-axis rotation sensors, indicated by "Sensor" to the amount indicated by "Value" (triggers the rotation indicator)
        Input: Address = 0-5, Value = 0-FFFF
        E.G. WR 0 F --> set the slow sensitivity of the Gx sensor, such that it triggers the rotation indicator when the STD exceeds 15% of the total variability range
        """
        pass

    def set_fms_constant_rotation(self, sensor, value):
        """
        Syntax: WRI <Sensor> <Value>
        Function: Set the fast motion sensitivity cosntant of any of the 6-axis rotation sensors, indicated by "Sensor" to the amunt indicated by "Value" (triggers the rotation indicator)
        Input: Address = 0-5, Value = 0-FFFF
        E.G.: WR O F --> set the fast sensitivity of the Gx sensor, such that it triggers the rotation indicator when the STD exceeds 15% of the total variability range
        """
        pass

    def set_sms_constant_quiet(self, sensor, value):
        """
        Syntax: WU <Sensor> <Value>
        Function: Set the slow motion sensitivity constant of any of the 6-axis rotation sensors, indicated by "Sensor" to the amount indicated by "Value" (triggers the quiet indicator)
        Input: Address = 0-5, Value = 0-FFFF
        E.G.: WU 0 F --> set the slow sensitivity of the Gx sensor, such that it triggers the quiet indicator when the STD exceeds 15% of the total variability range
        """
        pass

    def set_fms_constant_quiet(self, sensor, value):
        """
        Syntax: WUI <Sensor> <Value>
        Function: Set the fast motion sensitivity constant of any of the 6-axis rotation sensors, indicated by "Sensor" to the amount indicated by "Value" (triggers the quiet indicator)
        Input: Address = 0-5, Value = 0-FFFF
        E.G.: WU 0 F --> set the fast sensitivity of the Gx sensor, such taht it riggers teh quiet indicator when the STD exceeds 15% of the total variability range
        """
        pass

    def run_pattern(self, sequence, number, pattern, times):
        """
        Syntax: WP <P sequence> <P number> <Pattern> <# of repeat times>
        Function: Set "Pattern" at the "P number" in the "P sequence" to run "# of repeat times".
        Input: P sequence=0-2, P number=0-0x13, Pattern = 0-0x15, # of repeat time = 0-0xFFFF. Pattern = 0xFFFF indicates the end of the pattern buffer.
        E.G.: WP 0 0 0 1 --> set the pattern 0 to be the first pattern in the pattern sequence 0 and run only 1 time
        """
        pass

    def run_sequence(self, number, sequence, milliseconds):
        """
        Syntax: WQ <Q number> <Sequence> <Time in ms>
        Function: Set the "Sequence" to be the "Q number" sequence to run for "Time in ms".
        Input: Q number = 0-9, Sequence = 0-2, Time in ms = 0-0xFFFFFFFF. Sequence 0xFFFF indicates the end of the pattern sequence buffer.
        E.G.: WQ 0 0 927C0 --> Set the pattern sequence 0 to be the first pattern sequence and run for 10 minutes.
        """
        pass
    
    
    def write_flash(self, address, value):
        """
        Syntax: WF <Address> <Value>
        Function: Write "Value" to flash location indicated by "Address"
        Input: Address = 0-80000, Value = 0-FFFF
        """
        pass

    def display_current_sensor_values(self):
        """
        Syntax: S
        Function: Display the current sensor values
        """
        pass

    def display_gamma_ray_reading(self):
        """
        Syntax: SG
        Function: Display the current gamma ray reading (CPS) and corresponding specturm
        """
        pass
    
    def save_gr_readings_to_flash(self, acquisition_number):
        """
        Syntax: SGB <# of acquisition>
        Function: Save GR readings to the flash during the data saving interval (refer to command TR in Time and Date commands section) times as indicated by "# of acquisition"
        E.G.: SGB 4 --> save GR reading 4 times to the flash per data saving interval.
        """
        pass

    def toggle_live_sensor_display(self):
        """
        Syntax: SL
        Function: Turn on/off sensor values live display (updated per second)
        """
        pass

    def set_max_pulse_inclination(self, value):
        """
        Syntax: SI <Value>
        Function: Set the max inclination for the inclination pulses. (inclination > max inclination, pulse 25 times)
        Input: Value=0-90
        E.G.: SI 5 --> max inclination = 5
        """
        pass

    def set_gamma_ray_threshold(self, value):
        """
        Syntax: STT <Value>
        Function: Set the threshold of gamma ray CPS, indicated by "Value", to zero the tool face.
        Input: Value=0-0xFFFF
        E.G.: TT 20 --> Tool face will be zeroed to the position, when gamma ray CPS exceeds 0x20.
        """
        pass

    def toggle_tool_face_zeroing(self):
        """
        Syntax: STR
        Function: Turn on/off the tool face zeroing function.
        """
        pass

    def set_threshold_inclination_unit(self, value):
        """
        Syntax: STG <Value>
        Function: Set the threshold inclination in unit of 0.1 degree, indicated by "Value", to switch to gravity tool face.
        Input: Value = 0-0xFFFF
        E.G.: STG 32 --> Switch to gravity tool face when inclination > 5 degrees.
        """
        pass

    def set_gravity_tool_offset(self, value):
        """
        Syntax: STGO <Value>
        Function: Set the offset of the gravity tool face, indicated by "Value".
        Input: Value=0-0xFFFF
        E.G.: STGO A --> Offset the gravity tool face by 10 degrees.
        """
        pass

    def set_magnetic_tool_threshold(self, value):
        """
        Syntax: STH <Value>
        Function: Set the threshold inclination in unit of 0.1 degree, indicated by "Value", to switch to magnetic tool face.
        Input: Value=0-0xFFFF
        E.G.: STH 32 --> Switch to magnetic tool face when inclination < 5 degrees.
        """
        pass

    def set_magnetic_tool_offset(self, value):
        """
        Syntax: STHO <Value>
        Function: Set the offset of teh magnetic tool face, indicated by "Value".
        Input: Value=0-0xFFFF
        E.G.: STHO A --> Offset the magnetic tool face by 10 degrees.
        """
        pass

    def set_cycle_time_divider(self, value):
        """
        Syntax: PD <Value>
        Function: Set cycle time divider to be "Value", this will shorten the cycle time as well as the frame time by the factor of "Value", pulse time is not affected.
        Input: Value=0-0xFFFF
        E.G.: PD 2 --> shorten the cycle time by half
        """
        pass

    def set_cycle_time_multiplier(self, value):
        """
        Syntax: PM <Value>
        Function: Set cycle time multiplier to be "Value", this will extend the cycle time as well as the frame time by the factor of "Value", pulse time is not affected.
        Input: Value=0-0xFFFF
        E.G.: PM 2 --> extend the cycle time by 2 times
        """
        pass

    def set_regular_pule_time(self, milliseconds):
        """
        Syntax: PI <Time in ms>
        Function: Set the regular pulse time to be "Time in ms", this does not affect the cycle time.
        Input: Value = 0-0xFFFF
        E.G.: PI C8 --> Set the pule time to be 200 ms.
        """
        pass

    def set_actual_pulse_time(self, milliseconds):
        """
        Syntax: PIC <Time in ms>
        Function: Set the actual pulse time of the 2/5 interleaved bar code to be "Time in ms", this does not affect the cycle time.
        Input: Value = 0-0xFFFF
        E.G.: PIC C8 --> Set the actual pulse time of the 2/5 interleaved bar code t obe 200ms.
        """
        pass

    def set_min_code_pulse_time_difference(self, milliseconds):
        """
        Syntax: PID <Time in ms>
        Function: Set the minimal time difference required between the actual pulse time and a code time of the 2/5 interleaved bar code to be "Time in ms"
        Input: Value=0-0xFFFF
        E.G.: PID F --> The 2/5 interleaved bar code time has to be at least 15ms longer than the actual pulse time (refer to command PIC)
        """
        pass
    
    def set_narrow_barcode_time(self, milliseconds):
        """
        Syntax: PIN <Time in ms>
        Function: Set the time of the 2/5 interleaved narrow bar code to be "Time in ms".
        Input: Value=0-0xFFFF
        E.G.: PIC 1FC -> Set the narrow code time of the 2/5 interleaved bar code to be 500 ms.
        """
        pass

    def set_wide_barcode_time(self, milliseconds):
        """
        Syntax: PIW <Time in ms>
        Function: Set the time of the 2/5 interleaved wide bar code to be "Time in ms".
        Input: Value=0-0xFFFF
        E.G.: PIC 1FC --> Set the narrow code time of the 2/5 interleaved bar code to be 500 ms.
        """
        pass

    def compensate_valve_closing_time(self, milliseconds):
        """
        Syntax: PIS <Time in ms>
        Function: Compensate the valve closing time for the 2/5 interleaved bar code by "Time in ms".
        Input: Value=0-0xFFFF
        E.G.: PIS 10 --> Compensate the valve closing time by 10ms (will add to the actual pulse time)
        """
        pass

    def compensate_valve_opening_time(self, milliseconds):
        """
        Syntax: PIO <Time in ms>
        Function: Compensate the valve opening time for the 2/5 interleaved bar code by "Time in ms".
        Input: Value=0-0xFFFF
        E.G.: PIS 10 --> Compensate the valve opening time by 10 ms (will deduct from the actual pulse time)
        """
        pass

    def set_sync_word_narrow_wide(self, bit_indicator):
        """
        Syntax: PYN <Bit indicator>
        Function: Set the sync word as the narrow or wide code time indicated by the bits in "Bit indicator"
        Input: Value=0-0xFFFF
        E.G.: PYN 0000 --> sync word all narrow code time
        """
        pass

    def set_sync_word_pulse_gap(self, bit_indicator):
        """
        Syntax: PYP <Bit indicator>
        Function: Set the sync word as the pulse or gap indicatd by the bits in "Bit indicator" 
        Input: Value = 0-0xFFFF
        E.G.: PYP 2150 --> sync word 0010000101010000 with "1" indicates pulse, "0" indicates gap
        """
        pass

    def set_sync_word_length(self, bit_number):
        """
        Syntax: PYI <# of bit>
        Function: Set the length of the sync word as indicated by the "# of bit"
        Input: Value=0-0x10
        E.G.: PYLE --> sync word length 14 (*combine PYN, PYP, and PYL to define the sync word
        """
        pass

    def set_pulse_stop_time(self, milliseconds):
        """
        Syntax: PS <Time in ms>
        Function: Set the pulse stop time to be "Time in ms". When stop pulsing, there will be one pulse per pulse stop time.
        Input: Value = 0-0xFFFFFFFF
        E.G.: PS 7530 --> Set the pulse stop time to be 30 seconds, in that case, there will be 1 pulse per 30 seconds during pulse stopping period.
        """
        pass

    def set_sequence_as_default(self, number):
        """
        Syntax: PQ <Q number>
        Function: Set the "Q number" sequence to be the default pattern sequence to run.
        Input: Value=0-2
        E.G.: PQ 0 --> Set sequence in teh sequence buffer 0 to be the default sequence to run.
        """
        pass
    
    def set_rotation_sensor_buffer(self, length):
        """
        Syntax: ORB <Value>
        Function: Set the buffer of the ration sensor to be the length indicated by "Value"
        Input: Value = 0-FF
        E.G.: ORB 14 --> set rotation sensor buffer size to be 30 bins.
        """
        pass

    def turn_on_rotation_indicator(self, count):
        """
        Syntax: ORT <Value>
        Function: Count time as indicated by "Value" before turning on rotation indicator.
        Input: Value = 0-FF
        E.G.: OR 14 --> count 30 times before turning on rotation indicator, each count is about 1 sec.
        """
        pass

    def turn_off_rotation_indicator(self, count):
        """
        Syntax: ORN <Value>
        Function: Count time as indicated by "Value" before turning off rotation indicator.
        Input: Value = 0-FF
        E.G.: OR 14 --> count 30 times before turning off rotation indicator, each count is about 1 sec.
        """
        pass

    def turn_on_quiet_indicator(self, count):
        """
        Syntax: OQT <Value>
        Function: Count time as indicated by "Value" before tunring on quiet indicator.
        """
        pass

class ToolSimulator(object):
    pass
