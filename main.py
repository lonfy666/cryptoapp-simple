import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import Qt, QSize
from design import Ui_MainWindow
import requests
from io import BytesIO

class CryptoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.coins = [
    {"symbol": "BTCUSDT", "icon": "https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/btc.png", "name": "Bitcoin"},
    {"symbol": "ETHUSDT", "icon": "https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/eth.png", "name": "Ethereum"},
    {"symbol": "BNBUSDT", "icon": "https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/bnb.png", "name": "Binance Coin"},
    {"symbol": "SOLUSDT", "icon": "https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/sol.png", "name": "Solana"},
    {"symbol": "XRPUSDT", "icon": "https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/xrp.png", "name": "Ripple"},
    {"symbol": "ADAUSDT", "icon": "https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/ada.png", "name": "Cardano"},
    {"symbol": "DOGEUSDT", "icon": "https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/doge.png", "name": "Dogecoin"},
    {"symbol": "DOTUSDT", "icon": "https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/dot.png", "name": "Polkadot"},
    {"symbol": "MATICUSDT", "icon": "https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/matic.png", "name": "Polygon"},
    {"symbol": "LTCUSDT", "icon": "https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/ltc.png", "name": "Litecoin"},
    {"symbol": "AVAXUSDT", "icon": "https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/avax.png", "name": "Avalanche"},
    {"symbol": "LINKUSDT", "icon": "https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/link.png", "name": "Chainlink"},
    {"symbol": "ATOMUSDT", "icon": "https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/atom.png", "name": "Cosmos"},
    {"symbol": "UNIUSDT", "icon": "https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/uni.png", "name": "Uniswap"},
    {"symbol": "XMRUSDT", "icon": "https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/xmr.png", "name": "Monero"},
    {"symbol": "ETCUSDT", "icon": "https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/etc.png", "name": "Ethereum Classic"},
    {"symbol": "XLMUSDT", "icon": "https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/xlm.png", "name": "Stellar"},
    {"symbol": "FILUSDT", "icon": "https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/fil.png", "name": "Filecoin"},
    {"symbol": "VETUSDT", "icon": "https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/vet.png", "name": "VeChain"},
    {"symbol": "ALGOUSDT", "icon": "https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/algo.png", "name": "Algorand"},
    {"symbol": "ICPUSDT", "icon": "https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/icp.png", "name": "Internet Computer"},
    {"symbol": "XTZUSDT", "icon": "https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/xtz.png", "name": "Tezos"},
    {"symbol": "AAVEUSDT", "icon": "https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/aave.png", "name": "Aave"},
    {"symbol": "GRTUSDT", "icon": "https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/grt.png", "name": "The Graph"},
    {"symbol": "QNTUSDT", "icon": "https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/qnt.png", "name": "Quant"},
    {"symbol": "EOSUSDT", "icon": "https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/eos.png", "name": "EOS"},
    {"symbol": "STXUSDT", "icon": "https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/stx.png", "name": "Stacks"},
    {"symbol": "THETAUSDT", "icon": "https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/theta.png", "name": "Theta Network"},
    {"symbol": "SANDUSDT", "icon": "https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/sand.png", "name": "The Sandbox"},
    {"symbol": "MANAUSDT", "icon": "https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/mana.png", "name": "Decentraland"},
    {"symbol": "CHZUSDT", "icon": "https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/chz.png", "name": "Chiliz"},
    {"symbol": "CRVUSDT", "icon": "https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/crv.png", "name": "Curve DAO"},
    {"symbol": "APEUSDT", "icon": "https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/ape.png", "name": "ApeCoin"},
    {"symbol": "COMPUSDT", "icon": "https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/comp.png", "name": "Compound"},
    {"symbol": "MKRUSDT", "icon": "https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/mkr.png", "name": "Maker"},
    {"symbol": "SNXUSDT", "icon": "https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/snx.png", "name": "Synthetix"},
    {"symbol": "ZECUSDT", "icon": "https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/zec.png", "name": "Zcash"},
    {"symbol": "DASHUSDT", "icon": "https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/dash.png", "name": "Dash"},
    {"symbol": "ENJUSDT", "icon": "https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/enj.png", "name": "Enjin Coin"},
    {"symbol": "IOTAUSDT", "icon": "https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/miota.png", "name": "IOTA"},
    {"symbol": "ONTUSDT", "icon": "https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/ont.png", "name": "Ontology"},
    {"symbol": "WAVESUSDT", "icon": "https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/waves.png", "name": "Waves"},
    {"symbol": "NEOUSDT", "icon": "https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/neo.png", "name": "Neo"},
    {"symbol": "ONEUSDT", "icon": "https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/one.png", "name": "Harmony"},
    {"symbol": "GMTUSDT", "icon": "https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/gmt.png", "name": "STEPN"},
    {"symbol": "BATUSDT", "icon": "https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/bat.png", "name": "Basic Attention Token"},
    {"symbol": "XEMUSDT", "icon": "https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/xem.png", "name": "NEM"},
    {"symbol": "ZILUSDT", "icon": "https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/zil.png", "name": "Zilliqa"},
    {"symbol": "IOSTUSDT", "icon": "https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/iost.png", "name": "IOST"},
    {"symbol": "ANKRUSDT", "icon": "https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/ankr.png", "name": "Ankr"},
    {"symbol": "SCUSDT", "icon": "https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/sc.png", "name": "Siacoin"},
    {"symbol": "STORJUSDT", "icon": "https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/storj.png", "name": "Storj"},
    {"symbol": "HOTUSDT", "icon": "https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/hot.png", "name": "Holo"},
    {"symbol": "NKNUSDT", "icon": "https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/nkn.png", "name": "NKN"},
    {"symbol": "SUSHIUSDT", "icon": "https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/32/icon/sushi.png", "name": "SushiSwap"},
]
        for coin in self.coins:
            try:
                response = requests.get(coin["icon"])
                pixmap = QPixmap()
                pixmap.loadFromData(response.content)
                icon = QIcon(pixmap)
                
                self.ui.coinselector.addItem(icon, f"{coin['name']} ({coin['symbol']})", coin["symbol"])
            except Exception as e:
                print(f"Failed to load icon for {coin['symbol']}: {e}")
                self.ui.coinselector.addItem(f"{coin['name']} ({coin['symbol']})", coin["symbol"])

        self.ui.coinselector.setIconSize(QSize(24, 24))
        
        self.ui.updatebutton.clicked.connect(self.fetch_price)

    def fetch_price(self):
        select_coin = self.ui.coinselector.currentData()
        try:
            url = "https://api.binance.com/api/v3/ticker/price"
            response = requests.get(url, params={'symbol': select_coin})
            response.raise_for_status()
            price = float(response.json()['price'])
            self.ui.priceoutput.setText(f"{select_coin}: ${price:,.4f}")
        except Exception as e:
            self.ui.priceoutput.setText("Error fetching price")
            print("Error:", e)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CryptoApp()
    window.show()
    sys.exit(app.exec())