
class MotorOpenConfig(object):
    def __init__(self):
        self.acceleration_counter = 0
        self.initial_acceleration = 0
        self.maximal_acceleration = 0

    def set_acceleration_counter(self, value):
        """
        Syntax: MWUO <Value>
        Function: During acceleration to open position, motor acceleration constant incease by 1 every time a counter of "Value" expires.
        Input: Value = 0-0xFFFF
        E.G.: MWUO 5 --> During acceleration to motor open position, motor acceleration constant increase by 1, every time a counter of value 5 expires.
        """
        pass

    def set_initial_acceleration(self, value):
        """
        Syntax: MWUOI <Value>
        Function: Initial acceleration constant when motor is accelerating to open position.
        Input: Value = 0-15
        E.G.: MWUOM 1 --> Motor accelerate to open position, starting with acceleration constant of 1.
        """
        pass

    def set_maximal_acceleration(self, value):
        """
        Syntax: MWUOM <Value>
        Function: Maximal acceleration constant when motor is accelerating to open position.
        Input: Value=0-15
        E.G.: MWUOM F --> Allow the motor accelerate to maximal acceleration constant when accelerating to open position.
        """
        pass

    def set_deceleration_counter(self, value):
        """
        Syntax: MWDO <Value>
        Function: During de-acceleration to open position, motor acceleration constant decrease by 1, every time a counter of "Value" expires.
        Input: Value = 0-0xFFFF
        E.G.: MWDO 5 --> During deceleration to motor open position, motor acceleration constant decrease by 1 every time a counter of value 5 expires.
        """
        pass

    def set_minimal_deceleration(self, value):
        """
        Syntax: MWDON <Value>
        Function: Minimal deceleration constant when motor is decelerating to open position
        Input: Value=0-15
        E.G.: MWUSM 1 --> Allow the motor to decelerate to acceleration constant of 1 when accelerating to open position.
        """
        pass

class MotorShutConfig(object):
    def __init__(self):
        self.acceleration_counter = 0
        self.initial_acceleration = 0
        self.maximal_acceleration = 0


    def set_acceleration_counter(self, value):
        """
        Syntax: MWUS <Value>
        Function: During acceleraetion to shut position, motor acceleration constant increase by 1 every time a counter of "Value" expires.
        Input: Value=0-0xFFFF
        E.G.: MWUS 5 --> During acceleration to motor shut position, motor acceleration constant increase by 1, every time a counter of value 5 expires.
        """
        pass

    def set_initial_acceleration(self, value):
        """
        Syntax: MWUSI <Value>
        Function: Initial acceleration constant when motor is accelerating to shut position.
        Input: Value = 0-15
        E.G.: MWUOM 1 --> Motor accelerate to shut position, starting with acceleration constant of 1.
        """
        pass

    def set_maximal_acceleration(self, value):
        """
        Syntax: MWUSM <Value>
        Function: Maximal acceleration constant when motor is accelerating to shut position.
        Input: Value = 0-15
        E.G.: MWUSM F --> Allow the motor accelerate to maximal acceleration constant (15) when accelerating to shut position.
        """
        pass

    def set_deceleration_counter(self, value):
        """
        Syntax: MWDS <Value>
        Function: During deceleration to shut position, motor acceleration constant decrease by 1 every time a counter of "Value" expires.
        Input: Value = 0-0xFFFF
        E.G.: MWDS 5 --> During deceleration to motor shut position, motor acceleration constant decrease by 1 every time a counter of value 5 expires.
        """
        pass

    def set_minimal_deceleration(self, value):
        """
        Syntax: MWDSN <Value>
        Function: Minimal deceleration constant when motor is decelerating to shut position.
        Input: Value = 0-15
        E.G.: MWUSM 1 --> Allow the motor to decelerate to acceleration constant of 1 when accelerating to shut position
        """
        pass

    

class Motor(object):
    def read_load_profile(self):
        """
        Syntax: RD
        Function: Read the averaged motor load profile of calibration
        """
        pass

    def set_restart_step(self, value):
        """
        Syntax: MAS <Value>
        Function: Set the motor restart step to be the position counts indicated by "Value".
        Input: Value=0-0xFFFF
        E.G.: MAS 20 --> The motor will move back forward 20 position counts when restarting.
        """
        pass

    def set_restarting_acceleration(self, value):
        """
        Syntax: MAP <Value>
        Function: Set the motor restarting acceleration constant to be "Value"
        Input: Value=0-15
        E.G.: MAP F --> Motor will run with maximal acceleration to restart.
        """
        pass

    def set_freeze_counter(self, value):
        """
        Syntax: MFC <Value>
        Function: Set the motor freeze counter value to be "Value". Motor will freeze when counter expires, battery low mode activated.
        Input: Value = 0-0xFFFF
        E.G.: MFC 14 --> Set the motor freeze counter value to be 20, when counter expires, motor freezes and battery low mode activated.
        """
        pass

    def set_freeze_timer(self, value):
        """
        Syntax: MFR <Time in ms>
        Function: Set the motor freeze timer value to be "Time in ms". When timer expires, motor freeze counter will be reset to the default value.
        Input: Value=0-0xFFFFFFFF
        E.G.: MFR 927C) --> Set the motor freeze timer values to be 10 minutes.
        """
        pass

    def unfreeze(self):
        """
        Syntax: MFO 
        Function: Release motor from motor freeze, deactivate low battery mode.
        """
        pass

    def calibrate(self):
        """
        Syntax: ML
        Function: Calibrate motor, use "MC" to capture the motor first before executing "ML".
        """
        pass

    def set_calibration_acceleration_constant(self, value):
        """
        Syntax: MLP <Value>
        Function: Set initial motor calibration acceleration constant to be "Value"
        Input: Value=0-15
        E.G.: MLP3 --> Set the initial calibration acceleration constant to be 3.
        """
        pass
    
    def set_reference_load(self, value):
        """
        Syntax: MLL <Value>
        Function: Set the reference motor load to be "Value"
        Input: Value=0-0x0FFFF
        E.G.: MLL 20 --> Set the reference motor load for calibration to be "Value".
        """
        pass

    def set_open_position_target(self, value):
        """
        Syntax: MLO <Value>
        Function: Set the load target of motor open position as "Value"
        Input: Value=0-0xFFFF
        E.G.: MLO C0 --> The motor load at open position is no less than 0xC0
        """
        pass

    
    def set_shut_position_target(self, value):
        """
        Syntax: MLS <Value>
        Function: Set the load target of motor shut position as "Value"
        Input: Value=0-0xFFFF
        E.G.: MLS C0--> The motor load at shut position is no less than 0xC0.
        """
        pass

    def skip_position_counts(self, value):
        """
        Syntax: MLC <Value>
        Function: During calibration, sip the motor load of the position counts indicated by "Value", when changing motor running directions.
        Input: Value = 0-0xFFFF
        E.G.: MLC 6 --> Skip the motor load of the first 6 position counts during calibration. 
        """
        pass

    def display_current_calibration_status(self):
        """
        Syntax: MLT
        Function: Display the current calibration status, including the open and shut position.
        """
        pass

    def set_open_position_offset(self, value):
        """
        Syntax: MOF <Value>
        Function: Set motor open position offset to be "Value"
        Input: Value = 0-0xFFFF, signed integer
        E.G.: MOF FFFF --> set the motor open position offset to be -1
        """
        pass

    def set_shut_position_offset(self, value):
        """
        Syntax: MSF <Value>
        Function: Set motor shut position offset to be "Value"
        Input: Value=0-0xFFFF, signed integer
        E.G.: MSF 9 --> set the motor shut position offset to be 9
        """
        pass

    def toggle_switch_pattern_sequences(self):
        """
        Syntax: MY
        Function: Turn on/off the mode that motor switch pattern sequences according to the pattern sequence indicator.
        """
        pass

    def start_deceleration_at(self, value):
        """
        Syntax: MN <Value>
        Function: Motor start do decelerate when distance to target position is "Value" counts.
        Input: Value=0-0xFFFF
        E.G.: MN 5 --> motor will start to decelerate when it is 5 counts from target.
        """
        pass

    def stop_at_distance(self, value):
        """
        Syntax: MH <Value>
        Function: Motor stop when distance to target position is within "Value" counts.
        Input: Value = 0-0xFFFF
        E.G.: MH 2 --> motor stop, when it is within 5 counts from target.
        """
        pass

    def set_encoder_scale(self, value):
        """
        Syntax: ME <Value>
        Function: Set motor encoder scale to be "Value"
        Input: Value = 0-0xFFFF
        E.G.: ME 4 --> set encoder scale to be 4
        """
        pass

    def set_gear_numerator(self, value):
        """
        Syntax: MGN <Value>
        Function: Set motor gear numerator
        Input: Value=0-0xFFFF
        """
        pass

    def set_gear_denominator(self, value):
        """
        Syntax: MGD <Value>
        Function: Set motor gear denominator
        Input: Value = 0-0xFFFF
        """
        pass

    def capture_motor(self):
        """
        Syntax: MC
        Function: Capture motor
        """
        pass

    def motor_load_buffer(self):
        """
        Syntax: MD 
        Function: Display current motor load buffer
        """
        pass

    def release_motor(self):
        """
        Syntax: MR
        Function: Release motor
        """
        pass

    def motor_position(self):
        """
        Syntax: MP
        Function: Display current motor position
        """
        pass

    def move_to_poppet_open(self):
        """
        Syntax: MO
        Function: Motor move to poppet open position
        """
        pass

    def poppet_open_position(self):
        """
        Syntax: MOP
        Function: Display current poppet open position
        """
        pass

    def move_to_poppet_shut(self):
        """
        Syntax: MS 
        Function: Motor move to poppet shut position
        """
        pass

    def poppet_shut_position(self):
        """
        Syntax: MSP
        Function: Display current poppet shut position
        """
        pass

    def motor_target(self):
        """
        Syntax: MT
        Function: Display current motor target
        """
        pass        
