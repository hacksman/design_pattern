# coding: utf-8
# @Time : 2020/12/19 10:27 AM

from loguru import logger

# # 鸟 -> 定义一个抽象的类，定义 fly 方法，表示鸟儿会飞
#
# class AbstractBird:
#
#     def fly(self):
#         logger.info(f"I can fly")
#
#
# # 但是有一些鸟不会飞，比如鸵鸟。当然我们可以通过抛出异常的方式，说明鸵鸟不会飞
#
# class UnSupportMethodException(Exception):
#     pass
#
#
# class Ostrich(AbstractBird):
#     def fly(self):
#         raise UnSupportMethodException("I can not fly")
#
#
# # 这样做可以，但是不够优雅，还有很多其他的鸟类不会飞，难道每一个里面都要抛出不会飞的异常？
#
# # 那我们如果通过多继承处理呢？将抽象鸟类，再细分为不会飞的鸟和会飞的鸟
#
# class AbstractFlyableBird(AbstractBird):
#     def fly(self):
#         logger.info(f"I can fly")
#
#
# class AbstractUnFlyableBird(AbstractBird):
#     def fly(self):
#         raise UnSupportMethodException(" I can not fly")
#
#
# # 然后具有会飞能力的鸟，继承会飞类，不会飞的，继承不会飞的类
# class Sparrow(AbstractFlyableBird):
#     pass


# 但是如果我们有其他的行为呢？比如是否会叫，这个时候出现了四种类：不会飞不会叫，不会飞会叫，会飞不会叫，会飞会叫。ok 还不算多，那我们再加一个行为呢？
# 显然，这样做会造成代码里面各种类，而且多继承之后，我们具体实现，要去父类看具体的实现细节，可读性和可维护性大打折扣

# 我们可以通过使用组合、接口、委托解决以上问题
# 接口：has-a，不做具体实现，只表达是否具有某种特征

import abc
from abc import ABCMeta
from abc import abstractmethod


class Flyable(metaclass=ABCMeta):

    @classmethod
    @abstractmethod
    def fly(cls):
        pass


class Tweetable(metaclass=ABCMeta):

    @classmethod
    @abstractmethod
    def tweet(cls):
        pass


class FlyAbility(Flyable):

    def fly(cls):
        logger.info("I can fly")


class Tweetablity(Tweetable):

    def tweet(cls):
        logger.info(f"I can tweet")


class Sparrow(FlyAbility, Tweetablity):
    __fly_ability = FlyAbility()  # 组合
    __tweet_ability = Tweetablity()  # 组合

    def fly(cls):
        cls.__fly_ability.fly()  # 委托

    def tweet(cls):
        cls.__tweet_ability.tweet()  # 委托


if __name__ == '__main__':
    spa = Sparrow()
    spa.fly()
    spa.tweet()

# 理论上，我们完全可以通过代理、委托和组合替代掉继承，复杂的工程，应该尽可能少用继承，而改用组合

# 非理论上，得根据项目情况决定是否使用继承或者组合，如果确定之后继承关系稳定，不会有多少修改，且继承关系不深（不超过三层）就可以使用继承