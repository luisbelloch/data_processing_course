#!/usr/bin/env ruby

require 'socket'
require 'csv'

@simbolos = ["MSFT", "IBM", "GOOG", "YHOO", "APPL", "SIFI", "NWBO", "CRTO", "LAMR", "EYES", "ONTX", "FWP", "XXIA", "ASBB", "FTHI", "LSCC", "MRTN", "MBII", "EARS", "FTLB", "PBSK", "PRPH", "VRTU", "QUIK", "RYAAY", "WPRT", "HNNA", "CBSHP", "ADHD", "SGEN", "EZCH", "ADXS", "SNMX", "AXAS", "ASEI", "PME", "AGII", "HABT", "SCAI", "WMAR", "BKSC", "ORBK", "FTSL", "JRVR", "PMTS", "PRTO", "BLVDU", "XCRA", "LIND", "DTLK", "CERS", "TSC", "SONA", "CFGE", "CMFN", "PHIIK", "ASCMA", "HCAP", "HBANP", "WOWO", "KWEB", "CRDS", "EMIF", "MAUI", "LIVE", "ADRD", "AMAT", "EXLS", "FEIC", "QUNR", "LABL", "CDOR", "FRSH", "MTSI", "PCYO", "GOODN", "PRGX", "VXUS", "PCRX", "MAGS", "ALOG", "CYTR", "WHLR", "XBKS", "JRJC", "MDM", "HFBC", "CHY", "WSBF", "WOOD", "GULF", "FNWB", "GMLP", "NATR", "RDI", "RPRX", "EMMS", "ZFGN", "ADI", "BBH"]
# @simbolos = CSV.read('data/nasdaq.csv', {:col_sep => "|"}).drop(2).map { |s| s[0] }
@emitted = {}

def generar_stock
  name = @simbolos.sample
  price = 20 + Random.rand(200.0)
  if @emitted.has_key? name
    current = @emitted[name]
    price = current + (current * ([1,-1].sample * Random.rand(0.01)))
  end
  @emitted[name] = price
  "#{name},#{price.round(2)}"
end

def envio_continuo(cliente)
  loop do
    [1,3,5,7].sample.times do
      stock = generar_stock
      puts stock
      cliente.puts stock
    end
    sleep Random.rand(2.0)
  end
end

def main
  server = TCPServer.new 9999
  puts "Escuchando en tcp://localhost:9999..."

  loop do
    Thread.start(server.accept) do |cliente|
      envio_continuo cliente
    end
  end
end

if __FILE__ == $0
  main()
  50.times { |n| puts generar_stock }
end
