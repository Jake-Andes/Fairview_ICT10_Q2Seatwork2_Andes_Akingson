from pyscript import document, display # type: ignore

def adding_numbers(e):
    Fname = document.getElementById("Fname").value or ""
    Lname = document.getElementById("Lname").value or ""
    try:
        Math = float(document.getElementById("Math").value or 0)
        Filipino = float(document.getElementById("Filipino").value or 0)
        Science = float(document.getElementById("Science").value or 0)
        ICT = float(document.getElementById("ICT").value or 0)
        English = float(document.getElementById("English").value or 0)
        PE = float(document.getElementById("PE").value or 0)
    except Exception:
        display("Please enter valid numeric grades.", target="output1")
        return

    full_name = f"{Fname} {Lname}"
    weighted_sum = (Science * 5 + Math * 5 + English * 5 + Filipino * 3 + ICT * 2 + PE * 1)
    total_units = (5 * 3) + 3 + 2 + 1
    gwa = weighted_sum / total_units 
    summary = (
        f"Science: {Science}\n"
        f"Math: {Math}\n"
        f"English: {English}\n"
        f"Filipino: {Filipino}\n"
        f"ICT: {ICT}\n"
        f"PE: {PE}\n"
    )

    output = f"{full_name}{summary}\nYour general weighted average is {gwa:.2f}"
    display(output, target="output1")
# the try: and except: and the /n are from copilot because it allowed my code to display properly without errors