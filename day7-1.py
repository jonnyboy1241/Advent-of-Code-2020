'''
--- Day 7: Handy Haversacks ---
You land at the regional airport in time for your next flight. In fact, it looks like you'll even have time to grab some food: all flights are currently delayed due to issues in luggage processing.

Due to recent aviation regulations, many rules (your puzzle input) are being enforced about bags and their contents; bags must be color-coded and must contain specific quantities of other color-coded bags. Apparently, nobody responsible for these regulations considered how long they would take to enforce!

For example, consider the following rules:

light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.

These rules specify the required contents for 9 bag types. In this example, every faded blue bag is empty, every vibrant plum bag contains 11 bags (5 faded blue and 6 dotted black), and so on.

You have a shiny gold bag. If you wanted to carry it in at least one other bag, how many different bag colors would be valid for the outermost bag? (In other words: how many colors can, eventually, contain at least one shiny gold bag?)

In the above rules, the following options would be available to you:

A bright white bag, which can hold your shiny gold bag directly.
A muted yellow bag, which can hold your shiny gold bag directly, plus some other bags.
A dark orange bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
A light red bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.

So, in this example, the number of bag colors that can eventually contain at least one shiny gold bag is 4.

How many bag colors can eventually contain at least one shiny gold bag? (The list of rules is quite long; make sure you get all of it.)
'''

import re

processed_rules = None

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
        values = list(filter(None, [x.strip() for x in re.split('bag[s]?|[0-9,.]', split1[1])]))

        processed_rules[key] = values

    return processed_rules


def confirm_bag(rule, confirmed_bags):
    global processed_rules

    if rule in confirmed_bags:
        return True

    if rule == 'no other':
        return False

    items = processed_rules[rule]

    if 'shiny gold' in items:
        return True

    for item in items:
        if confirm_bag(item, confirmed_bags):
            return True
    
    return False




def calc_shiny_gold_count():
    global processed_rules
    confirmed_bags = []

    for rule in processed_rules:
        if confirm_bag(rule, confirmed_bags):
            confirmed_bags.append(rule)

    
    return len(confirmed_bags)


def main():
    global processed_rules

    rules = read_rules()
    processed_rules = process_rules(rules)
    num_approved_bags = calc_shiny_gold_count()
    print(num_approved_bags)


if __name__ == '__main__':
    main()
