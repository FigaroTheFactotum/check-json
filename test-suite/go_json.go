package main

import (
	"encoding/json"
	"log"
	"os"
)

func main() {
	var data interface{}

	e := log.New(os.Stderr, "", 0)
	dec := json.NewDecoder(os.Stdin)
	dec.UseNumber()

	if err := dec.Decode(&data); err != nil {
		e.Println(err)

		os.Exit(1)
	}

	enc := json.NewEncoder(os.Stdout)
	if err := enc.Encode(data); err != nil {
		e.Println(err)

		os.Exit(1)
	}

	os.Exit(0)
}
