# Todo

## Features
- [ ] Register
- [ ] Login

- [ ] List Items
- [ ] Filter Items
- [ ] Paging Item list

- [ ] Cart
- [ ] Wish List

- [ ] Buy
- [ ] Sell

- [ ] Store
- [ ] Auction
- [ ] BIN Auction

- [ ] Digital Coins
- [ ] Buy Digital Coin

## Pages:
- [ ] Register Page
- [ ] Login Page

- [ ] Index Page

- [ ] Item List Page
	- [ ] Search
	- [ ] Filter
	- [ ] Paging
	- [ ] Add to Cart
	- [ ] Add to Wish List
	- [ ] Coins

- [ ] Product Page
	- [ ] Details
	- [ ] Add to Cart
	- [ ] Add to Wish List
	- [ ] Coins

- [ ] Buy Coin Page
	- [ ] Buy
	- [ ] Packages

- [ ] Cart page
	- [ ] List Cart Items
	- [ ] Remove Items
	- [ ] Checkout

- [ ] Wishlist Page
	- [ ] List Wishlist Items
	- [ ] Remove Item

## Flow
#### Register page
- Register
- Login page

#### Login Page
- Login
- Register Page
- Index Page
- {Next} Page

#### Index Page
- Item List page
- Product page
- Buy Coin Page
- Cart page
- Wishlist Page
- Add to Cart
- Add to wishlist
- Logout

#### Items List page
- Product page
- Buy Coin Page
- Cart Page
- Wishlist Page
- Index Page
- Next
- Add to Cart
- Add to wishlist
- Logout

#### Product Page
- Items List page
- Buy Coin Page
- Cart Page
- Wishlist Page
- Index Page
- Add to Cart
- Add to wishlist
- Logout

#### Buy Coin Page
- Items List page
- Cart Page
- Wishlist Page
- Index Page
- Logout
- Buy

#### Cart Page
- Items List page
- Wishlist Page
- Buy Coin Page
- Index Page
- Logout
- Checkout
- Remove Item

#### Wishlist Page
- Items List page
- Cart Page
- Buy Coin Page
- Index Page
- Logout
- Remove Item

## Database

#### User(Django Default)

#### Items
- Id
- Name
- Summary
- Details
- Rarity
- Type
- Image

#### Listing
- Id
- Type
- Status
- Price
- Stock
- Listing
- Expiration
- SellerId
- BuyerId

#### Bids
- Id
- ItemId
- UserId
- Price
- Time

#### Wishlist
- Id
- UserId
- ItemId
- Created

#### Cart
- Id
- UserId
- ListingId
- Quantity