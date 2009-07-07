
class Time(object):
    def __init__(self, year, month, day, hour, second):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.second = second

class Tool(object):
    def __init__(self):
        self.time = None

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

    def read_motor_load_profile(self):
        """
        Syntax: RD
        Function: Read the averaged motor load profile of calibration
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
    
    
        
    
        
        
    
    

class ToolSimulator(object):
    pass
