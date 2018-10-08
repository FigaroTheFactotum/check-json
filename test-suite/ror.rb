#!/usr/bin/env ruby
require 'active_support/all'

json = ActiveSupport::JSON

text = $stdin.read

data = json.decode(text)

puts json.encode(data)
