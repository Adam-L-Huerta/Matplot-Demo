import matplotlib.pyplot as plt

'''
# --- Video 1 Example ---
years = [1950, 1955, 1960, 1965, 1970,
         1975, 1980, 1985, 1990, 1995,
         2000, 2005, 2010, 2015]

population = [2.5, 2.7, 3.0, 3.3, 3.6,
              4.0, 4.4, 4.8, 5.3, 5.7,
              6.1, 6.5, 6.9, 7.3]

deaths = [1.1, 1.2, 1.3, 1.4, 1.5,
          1.6, 2.7, 2.8, 2.9, 3.2,
          3.4, 3.6, 4.2, 5.6]

# plt.plot(years, population, color=(255/255, 100/255, 100/255))
# plt.plot(years, deaths, "--")
# plt.ylabel("Population in Billions")
# plt.xlabel("Year")
# plt.title("Population Growth")


# --- Video 2 ---
# lines = plt.plot(years, population, years, deaths)
# plt.grid(True)

# plt.setp(lines, color=(1, 0.2, 0.8), marker="o")
# plt.show()
'''

### Let's Make Pie (charts) ###

labels = 'Python', 'C++', 'Ruby', 'Java', 'PHP', 'Perl'
sizes = [33, 52, 16, 17, 34, 44]
separated = (.1, 0, 0, 0, 0, 0)

plt.pie(sizes, labels=labels, autopct='%1.1f%%', explode=separated)
plt.axis('equal')
plt.show()