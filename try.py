def analyze_logs(log_data):
    # Split ang multi-line string by newline at alisin ang empty lines
    lines = [line.strip() for line in log_data.strip().split("\n") if line.strip()]

    total_requests = len(lines)
    status_counts = {}
    ip_addresses = set()

    for line in lines:
        parts = line.split(" ")

        # Kunin ang IP address (laging nasa unang element)
        ip = parts[0]
        ip_addresses.add(ip)

        # Kunin ang status code (laging nasa dulo)
        status = int(parts[-1])
        status_counts[status] = status_counts.get(status, 0) + 1

    return {
        "total_requests": total_requests,
        "status_counts": status_counts,
        "ip_addresses": sorted(list(ip_addresses))
    }


# --- Interactive Part gamit ang user_input ---
print("I-paste ang iyong logs dito (I-type ang 'END' sa bagong line pagkatapos tapusin):")
user_lines = []
while True:
    try:
        line = input()
        if line.strip() == "END":
            break
        user_lines.append(line)
    except EOFError:
        break

# Pagdugtungin ang mga nilagay ng user gamit ang newline
user_input_logs = "\n".join(user_lines)

if user_input_logs.strip():
    result = analyze_logs(user_input_logs)
    print("\n--- Resulta ng Analisis ---")
    print(result)
else:
    print("Walang inilagay na logs.")