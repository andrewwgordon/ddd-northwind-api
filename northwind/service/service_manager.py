from typing import Union,List
from northwind.seedwork.i_command import ICommand
from northwind.seedwork.I_event import IDomainEvent
from northwind.domain.product_detail import ProductDetail,IProductDetailRepository,SearchForProductDetails
import logging

log=logging.getLogger(__name__)

Message = Union[ICommand,IDomainEvent]

class ServiceManager:

    def __init__(self,product_detail_repository: IProductDetailRepository) -> None:
        self.__product_detail_repository = product_detail_repository
        self.command_handlers={
            SearchForProductDetails: self.__search_product_catalog
        }

    def handle(self,message: Message):
        results = []
        queue = [message]
        while queue:
            message = queue.pop(0)
            if isinstance(message,ICommand):
                results = self.__handle_command(message,queue)
            elif isinstance(message,IDomainEvent):
                self.__handle_event(message,queue)
            else:
                error_mesg = f'{message} is not a registered Comamnd or Domain Event'
                log.error(error_mesg)
                raise Exception(error_mesg)
        return results
    
    def __handle_event(self,
        event: IDomainEvent,
        queue: List[Message]
        ):
        error_msg = 'Event management is not implemented'
        log.error(error_msg)
        raise NotImplementedError(error_msg)
    
    def __handle_command(self,
        command: ICommand,
        queue: List[Message]
        ):
        try:
            handler = self.command_handlers[type(command)]
            result = handler(command)
            return result
        except Exception as ex:
            error_msg = 'Exception handling command %s'.format(command)
            log.error(error_msg)
            raise Exception(error_msg)

    def __search_product_catalog(self,
            search_product_details: SearchForProductDetails
        ) -> List[ProductDetail]:
        try:
            return self.__product_detail_repository.find(
                search_product_details.name,
                search_product_details.unit_price_from,
                search_product_details.unit_price_to,
                search_product_details.category_name
            )
        except Exception:
            raise



