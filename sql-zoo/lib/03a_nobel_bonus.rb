# == Schema Information
#
# Table name: nobels
#
#  yr          :integer
#  subject     :string
#  winner      :string

require_relative './sqlzoo.rb'

def physics_no_chemistry
  # In which years was the Physics prize awarded, but no Chemistry prize?
  execute(<<-SQL)
    SELECT DISTINCT
      a.yr
    FROM nobels a
    LEFT JOIN (SELECT yr FROM nobels WHERE subject = 'Chemistry') b
      ON a.yr = b.yr
    WHERE a.subject = 'Physics' AND b.yr IS NULL
  SQL
end
