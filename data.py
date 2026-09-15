NON_TIMES = {"NT", "DQ", "NS", "SCR"}

def parse_time(raw):
    if raw is None:
        return None

    cleaned = raw.strip().upper()

    if not cleaned:
        return None

    if cleaned in NON_TIMES:
        return None

    try:
        if ":" in cleaned:
            parts = cleaned.split(":")
            if len(parts) != 2:
                return None
            minutes = float(parts[0]) * 60
            seconds = float(parts[1])
            return round(minutes + seconds, 2)

        else:
            return float(cleaned)
    except ValueError:
        return None

def validate_prog(y1, y2, y3, threshold=0.25):
    pass

def compute_improvement(df):
    pass

def fit_pop_params(improvements):
    pass