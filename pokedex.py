import requests
import json

def get_evolution(pokemon_name):
	url = f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_name.lower()}"
	response = requests.get(url)
	if response.status_code == 200:
		data = response.json()
		evo_url = data['evolution_chain']['url']
		evo_response = requests.get(evo_url)
		evo_data = evo_response.json()

		chain = evo_data['chain']
		print(f"\n🔥 {pokemon_name.capitalize()} Evolution Chain:")

		current = chain
		while current:
			name = current['species']['name'].capitalize()
			if current['evolves_to']:
				detail = current['evolves_to'][0]['evolution_details'][0]
				level = detail.get('min_level') or 'Special condition'
				print(f" {name} → evolves at level {level}")
				current = current['evolves_to'][0]
			else:
				print(f" {name} → final form")
				current = None
	else:
		print(f"Pokémon '{pokemon_name}' not found.")



def main():
	while True:
		pokemon_name = input("\nEnter a Pokémon name to see its evolution chain (or 'exit' to quit): ")
		if pokemon_name.lower() == 'exit':
			print("Goodbye!")
			break
		get_evolution(pokemon_name)

main()