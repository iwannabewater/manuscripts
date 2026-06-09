.PHONY: verify verify-network

verify:
	node scripts/verify_repo.mjs

verify-network:
	node scripts/verify_repo.mjs --network
