import math

def generate_number(squad, n):
    # TODO: complete
    if n not in squad:
        return n
    elif n in squad:
        lowest = []
        for num in squad:
            if n - num >= 0:
                new = int(f"{num}{n - num}")
                if new not in squad:
                    lowest.append(new)
        if not lowest or len(str(min(lowest))) > 2:
            return None
        elif len(str(min(lowest))) <= 2:
            return min(lowest)