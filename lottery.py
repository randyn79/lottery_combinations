#!/usr/bin/env python3

import itertools
import csv
import math

def lottery_combinations(balls_drawn, total_balls, special_balls_drawn, total_special_balls):
    """
    Calculate the number of lottery combinations.
    
    balls_drawn: Number of balls drawn from the main pool of balls.
    total_balls: Total number of balls in the main pool of balls (the ball # with the highest value).
    special_balls_drawn: Number of special balls drawn (like a mega ball or power ball).
    total_special_balls: Total number of special balls (the ball # with the highest value in this pool).
    yields: All possible lottery number combinations.
    """
    for balls in itertools.combinations(range(1,total_balls + 1), balls_drawn):
        for special_balls in itertools.combinations(range(1, total_special_balls + 1), special_balls_drawn):
            yield list(balls) + list(special_balls)

def lottery_stats(balls_drawn, total_balls, special_balls_drawn, total_special_balls, ticket_cost):
    """Estimates and prints stats related to the number of combinations."""
    num_combinations = math.comb(total_balls, balls_drawn) * math.comb(total_special_balls, special_balls_drawn)
    print()
    print(f'There are {num_combinations:,} different combinations of numbers in this lottery')
    print()
    print(f'At ${ticket_cost:,.2f} per ticket, to buy every combination of numbers, it would')
    print(f'cost ${num_combinations * ticket_cost:,.2f}.')
    print()
    print(f'Assuming you were the only jackpot winner, anything you won over the amount of')
    print(f'the cost of buying the tickets would be profit.')
    print()

def combinations_to_csv(balls_drawn, special_balls_drawn, combinations):
    """Writes all of the possible lottery combinations to a csv file as they are generated."""
    header = [f'Ball {i}' for i in range(1, balls_drawn + 1)]
    header += [f'Special Ball {i}' for i in range(1, special_balls_drawn + 1)]

    with open('lottery-combinations.csv', 'w', newline='') as data:
        writer = csv.writer(data)
        writer.writerow(header)
        for combo in combinations:
            writer.writerow(combo)

if __name__ == "__main__":
    balls_drawn = int(input('How many balls are drawn in this lottery? '))
    total_balls = int(input('How many total balls are in the pool? '))
    special_balls_drawn = int(input('How many special balls are drawn (mega ball, power ball, etc)? '))
    total_special_balls = int(input('How many special balls are in the pool? '))
    ticket_cost = float(input('How much does each ticket cost? '))

    # Show lottery statistics
    lottery_stats(balls_drawn, total_balls, special_balls_drawn, total_special_balls, ticket_cost)
    
    export_choice = input('Do you want to export the lottery combinations to CSV? (Enter y for yes or n for no) ').casefold()

    if export_choice == 'y':
        combinations = lottery_combinations(balls_drawn, total_balls, special_balls_drawn, total_special_balls)
        combinations_to_csv(balls_drawn, special_balls_drawn, combinations)
        print('Lottery combinations have been saved as lottery-combinations.csv')
    
