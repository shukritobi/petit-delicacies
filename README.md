# Petit Delicacies

Static ecommerce proposal. Deploy in Settings > Pages > Deploy from a branch > main > / (root).

Preview only: product prices and shipping eligibility are illustrative; no live orders, payment or data submission. Owner dashboard demo at dashboard.html.

Production: merchant verifies catalog, photo rights, legal business details, stock, shipping, allergens and pricing. Use Cloudflare Worker + D1, authenticated dashboard, server-authoritative checkout, CHIP Collect hosted payments and independently verified idempotent webhooks. SS Digital Labs commission proposed at 15% of discounted eligible merchandise subtotal, excluding shipping and refunds. CHIP Send aggregate payouts require merchant consent and provider approval; otherwise weekly invoice. No confirmed native split between separate CHIP accounts. No credentials in GitHub Pages. Test all payment, refund, reconciliation and security flows before enabling production.

Media source manifest: assets/media-sources.json. Store approved original JPEGs in assets/ with the matching source keys. Remote media URLs may expire and are temporary fallbacks. Obtain permission before production use.