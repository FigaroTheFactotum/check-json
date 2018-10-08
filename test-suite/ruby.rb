#!/usr/bin/env ruby
require 'json'

text = $stdin.read

data = JSON.parse(text)

puts data.to_json
