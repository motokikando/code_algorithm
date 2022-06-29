# n, m = gets.split(" ").map(&:to_i)
# ary = n.times.map{gets.split.map(&:to_i)}

#n, m に代入
#
#m.times do で　m回ループ


n, m = gets.split.map(&:to_i)
list = ((n == 1 ? "0" : "1" << ("0" * n.pred))...("1" << ("0" * n))).lazy
m.times do
    s, c = gets.split
    list = list.select { |str| str[s.to_i-1] == c }
  end

puts list