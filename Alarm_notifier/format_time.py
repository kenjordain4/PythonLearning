def format_input_time(hour,minute):
    period="AM" if hour <12 else "PM"
    hour_12=hour%12
    if hour_12==0:
        hour_12=12
    return f"{hour_12:02d}:{minute:02d} {period}"
