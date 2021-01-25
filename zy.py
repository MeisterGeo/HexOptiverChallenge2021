import time

from optibook.synchronous_client import Exchange

import logging
logger = logging.getLogger('client')
logger.setLevel('ERROR')

print("Setup was successful.")


#compare the bid and ask prices of the two instruments


e = Exchange()
a = e.connect()

#instrument_limit = 400


def get_info():
    positions = e.get_positions()
    for p in positions:
        print(p, positions[p])
    pnl = e.get_pnl()
    print("current pnl is",pnl)
    for instrument_id in ['PHILIPS_A', 'PHILIPS_B']:
        outstanding = e.get_outstanding_orders(instrument_id)
        for o in outstanding.values():
            print(f"Outstanding order: order_id({o.order_id}), instrument_id({o.instrument_id}), price({o.price}), volume({o.volume}), side({o.side}) 10")


#result = e.insert_order('PHILIPS_B', price = price_B , volume=volume, side='ask', order_type='ioc')
#print(f"Order Id: {result} 1")


for instrument_id in ['PHILIPS_A', 'PHILIPS_B']:
    trades = e.poll_new_trades(instrument_id)
    for t in trades:
        print(f"[TRADED {t.instrument_id}] price({t.price}), volume({t.volume}), side({t.side})")




get_info()
# retreives the best bid/ask price from exchange. If the best bid price for B is greater than the best ask for A, sell to B and buy from A.
"""
def trades:
    for i in range(0,10000):
        
        positions = e.get_positions()
    
        try:
            
            if e.get_last_price_book('PHILIPS_B').bids[0].price > e.get_last_price_book('PHILIPS_A').asks[0].price:
                volume = e.get_last_price_book('PHILIPS_B').bids[0].volume
                price_B = round(e.get_last_price_book('PHILIPS_B').bids[0].price,3)
                price_A = round(e.get_last_price_book('PHILIPS_A').asks[0].price,3)
                
                if volume > 40:
                    volume = 40
                
                
                #if positions['PHILIPS_B'] > -instrument_limit or positions['PHILIPS_A'] < instrument_limit:
                   #print("sell B at:",price_B, " and buy A:",price_A, " for",volume," lots")
                    
                    result = e.insert_order('PHILIPS_B', price = price_B , volume=volume, side='ask', order_type='ioc')
                    print(f"Order Id: {result} 1")
                    
                    result = e.insert_order('PHILIPS_A', price = price_A, volume=volume, side='bid', order_type='ioc')
                    print(f"Order Id: {result} 2")
                    
                    
                    # clearing of positions using limit order from weighted mid price
                    
                    mid_price = (price_A+price_B)/2
                    
                    result = e.insert_order('PHILIPS_B', price = mid_price , volume=volume, side='bid', order_type='limit')
                    print(f"Order Id: {result} 3")
                    
                    result = e.insert_order('PHILIPS_A', price = mid_price, volume=volume, side='ask', order_type='limit')
                    print(f"Order Id: {result} 4")
                    
                    get_info()
                    
                    return(mid_price)
                
                    
            
        except IndexError:
            pass
        
        # does the same thing as above but in the reverse direction
        
        try:
            if e.get_last_price_book('PHILIPS_B').asks[0].price < e.get_last_price_book('PHILIPS_A').bids[0].price:
                volume = e.get_last_price_book('PHILIPS_B').asks[0].volume
                price_B = round(e.get_last_price_book('PHILIPS_B').asks[0].price,3)
                price_A = round(e.get_last_price_book('PHILIPS_A').bids[0].price,3)
                if volume > 60:
                    volume = 60
            
                
                
                
                #if positions['PHILIPS_B'] < instrument_limit or positions['PHILIPS_A'] > -instrument_limit:
                    #print("buy B:",price_B, " and sell A:",price_A, " for",volume," lots")
                    
                    result = e.insert_order('PHILIPS_B', price = price_B , volume=volume, side='bid', order_type='ioc')
                    print(f"Order Id: {result} 5")
                    
                    result = e.insert_order('PHILIPS_A', price = price_A, volume=volume, side='ask', order_type='ioc')
                    print(f"Order Id: {result} 6")
                    
                    
                    # clearing of positions using limit order from weighted mid price
                    
                    mid_price = (price_A+price_B)/2
                    
                    result = e.insert_order('PHILIPS_B', price = mid_price , volume=volume, side='ask', order_type='limit')
                    print(f"Order Id: {result} 7")
                    
                    result = e.insert_order('PHILIPS_A', price = mid_price, volume=volume, side='bid', order_type='limit')
                    print(f"Order Id: {result} 8")
                   
                    get_info() 
                
                    
            
        except IndexError:
            pass
        
        if i%100 ==0:
            print(int(100*i/10000),"% Done")
            
        time.sleep(0.2)
    
    get_info()
    

mid_price = trades()

"""