package main

import (
	"fmt"
	"os"

	tmd "go101.org/tmd.go"
)

func main() {
	if len(os.Args) < 3 || len(os.Args)%2 == 0 {
		fmt.Fprintln(os.Stderr, "usage: tmd-renderer <input.tmd> <output.html> [<input.tmd> <output.html> ...]")
		os.Exit(2)
	}

	lib, err := tmd.NewLib()
	if err != nil {
		fatal(err)
	}
	defer lib.Destroy()

	for i := 1; i < len(os.Args); i += 2 {
		input, err := os.ReadFile(os.Args[i])
		if err != nil {
			fatal(err)
		}
		output, err := lib.GenerateHtmlFromTmd(input, tmd.HtmlGenOptions{
			EnabledCustomApps: "html",
			RenderRoot:        true,
		})
		if err != nil {
			fatal(err)
		}
		if err := os.WriteFile(os.Args[i+1], output, 0o644); err != nil {
			fatal(err)
		}
	}
}

func fatal(err error) {
	fmt.Fprintln(os.Stderr, err)
	os.Exit(1)
}
