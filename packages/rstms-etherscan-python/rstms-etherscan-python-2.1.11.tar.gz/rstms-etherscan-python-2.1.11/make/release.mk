### create a new github release

.release: $(wheel)
	gh release create v$(version) --generate-notes --target master
	gh release upload v$(version) $(wheel)
	touch $@

release: .release


release-clean:
	rm -f .release


release-sterile:
	@:
