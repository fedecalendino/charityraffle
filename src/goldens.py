from raffles import raffle_07


def generate_golden_tickets(policy_id: str, number: int, amount: int):
    for id in range(amount):
        asset_name = f"{number:02}RaffleGoldenTicket{id:04}"
        asset_name_encoded = asset_name.encode().hex()
        asset_id = f"{policy_id}{asset_name_encoded}".lower()

        print(f'        "{asset_id}": "{asset_name} (golden ticket raffle #{number})",')


raffle = raffle_07

generate_golden_tickets(raffle.policy_id, raffle.number, 271)
