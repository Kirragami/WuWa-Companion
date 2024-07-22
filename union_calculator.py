def calculate_time_to_target_level(current_level, current_xp, target_level):
   xp_requirements = [400, 500, 600, 1100, 1200, 1300, 1400,
      1500, 1600, 1600, 1650, 1650, 1700, 1700, 1700,
      1750, 1750, 1800, 1800, 2300, 2400, 2500, 2500,
      2500, 2700, 2900, 3000, 3200, 3400, 6500, 6700,
      6800, 7200, 7600, 8000, 8400, 9000, 9600, 10000,
      10200, 10400, 10600, 10800, 11200, 11600, 12000,
      12400, 12800, 13000, 13100, 13300, 13500, 13700,
      13900, 14100, 14300, 14500, 14700, 15700, 21600,
      21900, 22300, 23000, 23800, 24700, 26100, 27500,
      29400, 29400, 32400, 32800, 33500, 34500, 35600,
      37200, 39100, 41300, 44100, 47300]
   xp_per_day = 3800

   required_total_xp = sum(xp_requirements[current_level - 1 :target_level - 1]) - current_xp

   days_to_reach_target_level = required_total_xp // xp_per_day + 1

   return days_to_reach_target_level
