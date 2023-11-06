# == Schema Information
#
# Table name: countries
#
#  name        :string       not null, primary key
#  continent   :string
#  area        :integer
#  population  :integer
#  gdp         :integer

require_relative './sqlzoo.rb'

def highest_gdp
  # Which countries have a GDP greater than every country in Europe? (Give the
  # name only. Some countries may have NULL gdp values)
  execute(<<-SQL)
  SELECT name
  FROM countries
  WHERE gdp > (SELECT MAX(gdp) FROM countries WHERE continent ='Europe')
  SQL
end

def largest_in_continent
  # Find the largest country (by area) in each continent. Show the continent,
  # name, and area.
  execute(<<-SQL)
  SELECT c.continent, c.name, c.area
  FROM countries c
  JOIN (SELECT continent, max(area) AS area FROM countries GROUP BY continent) a
    ON c.continent = a.continent
    AND c.area = a.area
  SQL
end

def large_neighbors
  # Some countries have populations more than three times that of any of their
  # neighbors (in the same continent). Give the countries and continents.
  execute(<<-SQL)
    SELECT c.name, c.continent
    FROM countries c
    JOIN (SELECT continent, population, ROW_NUMBER() OVER (PARTITION BY continent ORDER BY population DESC) AS row_number FROM countries) a
      ON c.continent = a.continent
      AND a.row_number = 2
    WHERE c.population / 3 > a.population
  SQL
end
