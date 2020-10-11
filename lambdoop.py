### Our fundamental "thing"
# factory
ThingMaker = lambda dna : (lambda func, *args, **kwargs : func(dna, *args, **kwargs))
# methods
dna = lambda me, *args, **kwargs : me
# objects
alice = ThingMaker({})

### People
# factory
PeopleMaker = lambda name, hobby, parentDna={}, *args, **kwargs : ThingMaker({ **{ 'name': name, 'hobby': hobby }, **parentDna }, *args, **kwargs)
# methods
introduce = lambda me, *args, **kwargs : 'Hi! My name is {0}'.format(me['name'])
# objects
alice = PeopleMaker('alice', 'revolution')

### Debit/Credit Accounts
# factory
AccountMaker = lambda account_id, balance=0, parentDna={}, *args, **kwargs : (ThingMaker({ **{ 'account_id': account_id, 'balance': balance }, **parentDna }, *args, **kwargs))
# methods
account_id = lambda me, *args, **kwargs : me['account_id']
credit = lambda me, amount, *args, **kwargs : AccountMaker(me['account_id'], me['balance']+amount)
debit = lambda me, amount, *args, **kwargs : AccountMaker(me['account_id'], me['balance']-amount)
# objects
alice = AccountMaker('1', 50, alice(dna)) # to extend alice, we pass her old dna as the `parentDna`: `alice(dna)`
bob = AccountMaker('2', 30)



print(alice(dna))
print(alice(introduce))
print(bob(dna))
# have alice pay bob 15 (immutability -- so, redefine both alice and bob with their new balances)
alice = alice(debit, 15)
bob = bob(credit, 15)
print(alice(dna))
print(bob(dna))
