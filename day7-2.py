'''
--- Part Two ---
It's getting pretty expensive to fly these days - not because of ticket prices, but because of the ridiculous number of bags you need to buy!

Consider again your shiny gold bag and the rules from the above example:

faded blue bags contain 0 other bags.
dotted black bags contain 0 other bags.
vibrant plum bags contain 11 other bags: 5 faded blue bags and 6 dotted black bags.
dark olive bags contain 7 other bags: 3 faded blue bags and 4 dotted black bags.

So, a single shiny gold bag must contain 1 dark olive bag (and the 7 bags within it) plus 2 vibrant plum bags (and the 11 bags within each of those): 1 + 1*7 + 2 + 2*11 = 32 bags!

Of course, the actual rules have a small chance of going several levels deeper than this example; be sure to count all of the bags, even if the nesting becomes topologically impractical!

Here's another example:

shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.

In this example, a single shiny gold bag must contain 126 other bags.

How many individual bags are required inside your single shiny gold bag?
'''

import re

def read_rules():
    rules = []

    with open('data/day7.txt', 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break

            rules.append(line.strip('\n'))

    return rules


def process_rules(rules):
    processed_rules = {}

    for rule in rules:
        split1 = rule.split(' contain ')

        key = split1[0][:-5]
        values = list(filter(None, [x.strip() for x in re.split('bag[s]?|[,.]', split1[1])]))

        current_dict = {}

        for item in values:
            if item != 'no other':
                item_split = item.split(' ', 1)
                current_dict[item_split[1]] = int(item_split[0])

        processed_rules[key] = current_dict

    return processed_rules


def calc_num_bags(rule, processed_rules):
    included_bags = processed_rules[rule]
    num_bags = 1

    for next_rule in included_bags:
        try:
            value = included_bags[next_rule]
            num_bags += value * calc_num_bags(next_rule, processed_rules)
        except KeyError:
            pass
    
    return num_bags


def main():
    rules = read_rules()
    processed_rules = process_rules(rules)
    num_bags = calc_num_bags('shiny gold', processed_rules) - 1

    print(num_bags)


if __name__ == '__main__':
    main()
