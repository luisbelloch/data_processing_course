require 'csv'
require 'faker'
require 'time'

def gen_id alpha = 3, num = 10000
  ('A'..'Z').to_a.shuffle[0,alpha].join + (num + Random.rand(num - 1)).to_s
end

def time_rand from = 0.0, to = Time.now
  Time.at(from + rand * (to.to_f - from.to_f))
end

def credit_card
  (1..4).map { |i| 1000 + Random.rand(999) }.join('-')
end

def funds(m)
  (1..m).each do |n|
    amount = Random.rand(1000.0)
    parent = gen_id
    parent_name = Faker::Company.name

    divisions = Random.rand(5)
    positions = [0] + (0..divisions-1).map { |d| Random.rand(1.0) }.sort + [1]
    currency = ['USD', 'EUR', 'JPY', 'AUD', 'CAD', 'GBP'].sample
    positions.each_cons(2) do |pos|
      percent = pos[1] - pos[0]
      identifier = gen_id
      tx_time = time_rand Time.local(2010, 1, 1), Time.local(2010, 12, 31)
      puts [tx_time, parent_name, parent, identifier, currency, percent.round(3), amount*percent].join('|')
    end
  end
end

def ratings(m)
  peliculas = ["01", "02", "03", "78", "79", "815", "29", "310", "04", "05", "28", "73", "74", "75", "765", "76", "77", "780", "31", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "18", "19", "20", "210", "218", "219", "21", "220", "220", "223", "224", "225", "22", "23", "214", "215", "216", "217", "23", "240", "24", "24", "25", "26", "270", "320", "321", "322", "323", "211", "211", "213", "324", "311", "312", "315", "316", "418", "41", "422", "422", "422", "423", "423", "425", "42", "43", "44", "45", "317", "318", "325", "328", "33", "33", "342", "34", "35", "362", "36", "61", "620", "621", "622", "623", "624", "625", "62", "63", "64", "65", "66", "66", "68", "37", "38", "39", "410", "411", "712", "713", "714", "715", "716", "717", "718", "719", "71", "720", "412", "412", "414", "415", "416", "417", "418", "46", "47", "48", "49", "610", "610", "612", "613", "614", "615", "616", "617", "618", "619", "69", "710", "711", "722", "723", "724", "725", "72", "915"]
  (1..m).each do |n|
    fecha = (time_rand Time.local(2016, 2, 15), Time.local(2016, 2, 21)).utc.iso8601
    puts "#{peliculas.sample},#{Random.rand(100000)},#{Random.rand(5)},#{fecha}"
  end
end

def ships_and_containers(m, p)
  puts ['ship_imo', 'ship_name', 'country', 'departure', 'container_id', 'container_type', 'container_group', 'net_weight', 'gross_weight', 'owner', 'declared', 'contact', 'customs_ok'].join(";")
  container_codes = CSV.read('./iso-container-codes.csv').map { |m| m[0] }.drop(1)
  container_groups = CSV.read('./iso-container-groups.csv').map { |m| m[0] }.drop(1)
  (1..m).each do |n|
    ship_imo = gen_id(3, 1000000)
    ship_name = [Faker::Name.first_name, Faker::Address.city].sample
    divisions = (p*10) + Random.rand((p*10)-1)
    positions = [0] + (0..divisions-1).map { |d| Random.rand(1.0) }.sort + [1]
    total_weight = (1000*1000*1000) + Random.rand(999999999)
    country = Faker::Address.country_code
    departure = (time_rand Time.local(2016, 2, 15), Time.local(2016, 2, 21)).strftime("%Y%m%d#{n}")
    positions.each_cons(2) do |pos|
      container_id = gen_id(4, 1000000) # ISO 6346
      container_type = container_codes.sample
      container_group = container_groups.sample
      owner = Faker::Company.name
      percent = pos[1] - pos[0]
      net_weight = (total_weight*percent).round(2)
      gross_weight = ([0.05, 0.1, 0.03].sample * net_weight).round(2)
      declared = Faker::Commerce.department(5)
      contact = Faker::Internet.email
      customs_ok = ((1..10).to_a.map { |n| true } + [false]).sample
      puts [ship_imo, ship_name, country, departure, container_id, container_type, container_group, net_weight, gross_weight, owner, declared, contact, customs_ok].join(";")
    end
  end
end

def shop(m)
  puts ['tx_id', 'tx_time', 'buyer', 'currency_code', 'payment_type', 'credit_card_number', 'country', 'department', 'product', 'item_price', 'coupon_code', 'was_returned'].join('|')
  (1..m).each do |n|
    buyer = Faker::Name.name
    tx_id = gen_id(7, 100)
    tx_time = time_rand Time.local(2010, 1, 1), Time.local(2010, 12, 31)
    cc = credit_card()
    price = Faker::Commerce.price
    currency = ['USD', 'EUR', 'JPY', 'AUD', 'CAD', 'GBP'].sample
    payment = ['VISA', 'MASTERCARD', 'AMERICAN_EXPRESS', 'DANKORT', 'JCB', 'FORBRUGSFORENINGEN'].sample
    country = Faker::Address.country_code
    divisions = [0, 0, Random.rand(5)].sample
    positions = [0] + (0..divisions-1).map { |d| Random.rand(1.0) }.sort + [1]
    positions.each_cons(2) do |pos|
      percent = pos[1] - pos[0]
      item_price = (price*percent).round(2)
      department = Faker::Commerce.department(1, true)
      product = Faker::Commerce.product_name
      coupon = [false, false, true, false].sample
      coupon_code = ''
      if (coupon)
        coupon_code = gen_id(3,2)
      end
      returned = [false, false, false, 'defect', 'bounce', false, false, false, false].sample
      puts [tx_id, tx_time.utc.iso8601, buyer, currency, payment, cc, country, department, product, item_price, coupon_code, returned].join('|')
    end

  end
end

# shop(1000)
# ships_and_containers(20, 2)
# ratings(10000)
