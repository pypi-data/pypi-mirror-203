from typing import List
import quickfix
from datetime import datetime
from random import randint


class ClientOrder:
    __client_order_id = None
    __data_row = None

    def __init__(self, client_order_id: str, data_row: dict):
        self.__client_order_id = client_order_id
        self.__data_row = data_row

    def get_client_order_id(self) -> str:
        return self.__client_order_id

    def get_test_fields(self) -> List[str]:
        return self.__data_row['testField'].split(',')

    def get_message_type(self) -> str:
        return self.__data_row['msgType']

    def get_expected_message_type(self) -> str:
        return self.__data_row['outputMsgType']

    def get_value(self, fieldName: str):
        return self.__data_row[fieldName]

    def has_value(self, fieldName: str) -> bool:
        return fieldName in self.__data_row

    def create_fix_msg(self):
        message = quickfix.Message()
        header = message.getHeader()

        if self.__data_row.get('msgType'):
            if self.__data_row['msgType'] == 'empty':
                header.setField(quickfix.MsgType(''))
            else:
                header.setField(quickfix.MsgType(self.__data_row['msgType']))

        if self.__data_row.get('account'):
            if self.__data_row['account'] == 'empty':
                message.setField(quickfix.Account(''))
            else:
                message.setField(quickfix.Account(self.__data_row['account']))

        if self.__data_row.get('orderQty'):
            message.setField(quickfix.OrderQty(float(self.__data_row['orderQty'])))

        if self.__data_row.get('price'):
            message.setField(quickfix.Price(float(self.__data_row['price'])))

        if self.__data_row.get('ordType'):
            if self.__data_row['ordType'] == 'empty':
                message.setField(quickfix.OrdType(''))
            else:
                message.setField(quickfix.OrdType(self.__data_row['ordType']))

        if self.__data_row.get('side'):
            if self.__data_row['side'] == 'empty':
                message.setField(quickfix.Side(''))
            else:
                message.setField(quickfix.Side(self.__data_row['side']))

        if self.__data_row.get('symbol'):
            if self.__data_row['symbol'] == 'empty':
                message.setField(quickfix.Symbol(''))
            else:
                message.setField(quickfix.Symbol(self.__data_row['symbol']))

        if self.__data_row.get('tif'):
            message.setField(quickfix.TimeInForce(self.__data_row['tif']))

        if self.__data_row.get('currency'):
            if self.__data_row['currency'] == 'empty':
                message.setField(quickfix.Currency(''))
            else:
                message.setField(quickfix.Currency(self.__data_row['currency']))

        if self.__data_row.get('settlType'):
            if self.__data_row['settlType'] == 'empty':
                message.setField(quickfix.SettlType(''))
            else:
                message.setField(quickfix.SettlType(self.__data_row['settlType']))

        if self.__data_row.get('noPartyId'):
            if self.__data_row['noPartyId'] == "1":
                group = quickfix.Group(453, 448)
            else:
                groupOne = quickfix.Group(453, 448)
                groupTwo = quickfix.Group(453, 448)

        if self.__data_row.get('partyId'):
            if self.__data_row['partyId'] == 'empty':
                group.setField(quickfix.PartyID(''))
            else:
                if self.__data_row['noPartyId'] == "1":
                    group.setField(quickfix.PartyID(self.__data_row['partyId']))
                else:
                    groupOne.setField(quickfix.PartyID(self.__data_row['partyId']))
                    groupTwo.setField(quickfix.PartyID(self.__data_row['partyId']))

        if self.__data_row.get('partyIdSource'):
            if self.__data_row['partyIdSource'] == 'empty':
                group.setField(quickfix.PartyIDSource(''))
            else:
                if self.__data_row['noPartyId'] == "1":
                    group.setField(quickfix.PartyIDSource(self.__data_row['partyIdSource']))
                else:
                    groupOne.setField(quickfix.PartyIDSource(self.__data_row['partyIdSource']))
                    groupTwo.setField(quickfix.PartyIDSource(self.__data_row['partyIdSource']))

        if self.__data_row.get('partyRole'):
            if self.__data_row['partyRole'] == 'noTag':
                message.addGroup(group)
            elif self.__data_row['partyRole'] == 'noPartyGroup':
                pass
            else:
                if self.__data_row['noPartyId'] == "1":
                    group.setField(quickfix.PartyRole(int(self.__data_row['partyRole'])))
                    message.addGroup(group)
                else:
                    groupOne.setField(quickfix.PartyRole(int(self.__data_row['partyRole'])))
                    groupTwo.setField(quickfix.PartyRole(int(self.__data_row['partyRole'])))
                    message.addGroup(groupOne)
                    message.addGroup(groupTwo)

        if self.__data_row.get('tradSesReqId'):
            if self.__data_row['tradSesReqId'] == 'empty':
                message.setField(quickfix.TradSesReqID(''))
            elif self.__data_row['tradSesReqId'] == 'no tag':
                pass
            elif self.__data_row['tradSesReqId'] == 'yes':
                tradeReqId = str(randint(0, 100000)) + str(datetime.now().strftime('%M:%S.%f')[:-4])
                message.setField(quickfix.TradSesReqID(tradeReqId))
            else:
                message.setField(quickfix.TradSesReqID("12"))

        if self.__data_row.get('clOrdId') and self.__client_order_id is not None:
            message.setField(quickfix.ClOrdID(self.__client_order_id))

        if self.__data_row.get('trxTime'):
            self.setTransactionTime(message)

        return message

    def setTransactionTime(self, message):
        if self.__data_row['trxTime'] == 'yes':
            transactTime = quickfix.TransactTime()
            transactTime.setString(datetime.utcnow().strftime("%Y%m%d-%H:%M:%S.%f")[:-3])
            message.setField(transactTime)
        elif self.__data_row['trxTime'] == 'invalid':
            message.setField(quickfix.TransactTime(10))

    @staticmethod
    def __get_client_order_id(row, last_order) -> str:
        if row['clOrdId'] == 'yes':
            return str(randint(0, 100000)) + str(datetime.now().strftime('%M:%S.%f')[:-4])
        elif row['clOrdId'] == 'no tag':
            return None
        elif row['clOrdId'] == 'empty':
            return ''
        elif row['clOrdId'] == 'duplicate':
            if not last_order:
                raise Exception("Invalid usage. Cannot use 'duplicate' for client order id, when not previous orders "
                                "have been sent via this connection.")
            return last_order.get_client_order_id()
        else:
            return row['clOrdId']

    @staticmethod
    def from_table_row(row: dict, last_order) -> 'ClientOrder':
        client_order_id = ClientOrder.__get_client_order_id(row, last_order)
        return ClientOrder(client_order_id, row)
