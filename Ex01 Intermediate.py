month = {'jan': 'January',
         'feb': 'February',
         'mar': 'March',
         'apr': 'April',
         'may': 'May',
         'jun': 'June',
         'jul': 'July',
         'aug': 'August',
         'sep': 'September',
         'oct': 'October',
         'nov': 'November',
         'dec': 'December',
}

month_short = input("Give me 3 chars: ").lower()

print(month[month_short])
