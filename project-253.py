# --------------253 Proj----------------
from web3 import Web3
import time
 

ganache_url = 'http://127.0.0.1:7545'

web3_ganache_connection = Web3(Web3.HTTPProvider(ganache_url))

Alice_account = '0x87f0e2A9AEbB58a58dDE312a97437657A2FcD25a'
James_account = '0x0A7C0663576c217d5f0AF183053B26c80E65e140'
Ryan_account  = '0x0FD448A5C6ADC17c5a592502FFADCF307dC6B387'


nonce1 = web3_ganache_connection.eth.get_transaction_count(James_account)

transaction_data1 = {
    'nonce':nonce1,
    'to':James_account,
    'value':web3_ganache_connection.to_wei("2", 'ether'),
    'gas':21000,
    'gasPrice':web3_ganache_connection.to_wei(50,'gwei')
}

private_key1 = '0x76838d15ab25b427c8365e1dad03f20b5adca5d7df4f1a492f9f2e4a3faa8586'

singed_transaction1 = web3_ganache_connection.eth.account.sign_transaction(transaction_data1,private_key1)
transaction_hash1 = web3_ganache_connection.eth.send_raw_transaction(singed_transaction1.rawTransaction)

print(web3_ganache_connection.to_hex(transaction_hash1))



# -----------------
print('Wait for few seconds Transaction is in progress')
time.sleep(5)
# -----------------
nonce2 = web3_ganache_connection.eth.get_transaction_count(Ryan_account)

transaction_data2 = {
    'nonce':nonce2,
    'to':Ryan_account,
    'value':web3_ganache_connection.to_wei("3", 'ether'),
    'gas':21000,
    'gasPrice':web3_ganache_connection.to_wei(40,'gwei')
}

private_key2 = '0x746e7dfc773cfe9b4a544d2ad1d0d73dcefa38238eae5e90d42530a019b1058b'

singed_transaction2 = web3_ganache_connection.eth.account.sign_transaction(transaction_data2,private_key2)
transaction_hash2 = web3_ganache_connection.eth.send_raw_transaction(singed_transaction2.rawTransaction)

print(web3_ganache_connection.to_hex(transaction_hash2))

