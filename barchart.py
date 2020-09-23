import matplotlib.pyplot as plt


languages = ['Java', 'Python', 'PHP', 'Javascript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
colors = ['r' , 'g' , 'b', '#E61B87', 'c', '#0ABDFF' ]
popularity2 = [21.2, 22.6, 9.8, 7.5, 7.2, 6.3]


x_pos = range(len(languages))


plt.bar(x_pos,
        popularity,
        color='b',
        edgecolor='k',
        align='center',
        width=-0.45,
        zorder=10,
        label='2019')

plt.bar(x_pos,
        popularity2,
        color='r',
        edgecolor='k',
        align='edge',
        width=0.45,
        alpha=0.85,
        zorder=20,
        label='2020')

plt.xticks(x_pos, labels=languages)
plt.title('Popularity of Programming Languages')
plt.ylabel('Popularity in %')
plt.xlabel('Programming Language')
plt.grid(which='major', linestyle='-.', linewidth=1, color='k', zorder=0)
plt.minorticks_on()
plt.grid(which='minor' , linestyle=':', linewidth=0.5, color='gray', zorder=0)
plt.legend()
plt.text(3, 15, 'Test.',
         fontdict={'size': 14, 'weight': 'bold'},
         rotation=15)
plt.show()
