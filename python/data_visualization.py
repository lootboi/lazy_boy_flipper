from colors import yellow, white

import plotext as plt

def visualize_attributes(attributes):
    trait_type_array = []
    for attribute in attributes['attributes']:
        traits = attribute['traitType']
        trait_type_array.append(traits)
        types_array = []
        value_count = []
        for trait in attribute['values']:
            trait_type = trait['value']
            trait_type_count = trait['count']
            types_array.append(trait_type)
            value_count.append(trait_type_count)
        plt.simple_bar(types_array, value_count, width = 100, title = yellow + 'Distribution of ' + traits + ' types' + white)
        plt.show()
        print('\n')