# coding:utf-8
class RewardType:

    Test = -1
    Undefined = 0
    FB = 1  # 副本推图
    Lottery = 2  # 精灵召唤（含道具兑换）
    BuySP = 3  # 购买能量
    ExpandPetBox = 4  # 购买精灵背包空间
    SalePet = 5  # 卖出宠物
    EvolutionPet = 6  # 精灵进化
    BreedPet = 7  # 精灵升级
    TotalLoginReward = 8  # 累计登陆奖励
    SerialLoginReward = 9  # 连续登陆奖励
    Mail = 10  # 邮件
    SlateReward = 11  # 残经
    PvpGain = 12  # 竞技场获得
    ExplorePlayerReward = 13  #
    ExplorePetReward = 14  # 探索
    RetryFB = 15  # 推图副本复活
    FactionStrengthen = 16  # 公会强化
    RefreshFB = 17  # 重置副本
    Task = 18  # 任务
    # Signup = 19  # 签到（补签）
    Recharge = 20  # 充值
    SkyMall = 21  # 彩虹百货
    SilverMall = 22  # 迷宫商人
    GoldenMall = 23  # 迷宫商人
    ResolveGold = 24  # 购买金币
    PatchChange = 25  # 精灵碎片合成
    CleanRankCD = 26  # 清除挑战CD
    PvpMall = 27  # 联盟限时商店
    CleanFB = 28  # 扫荡
    CreateFaction = 29  # 创建公会
    DonateFaction = 30  # 公会贡献
    LearnFaction = 31  # 学习公会技能
    PetPaltform = 32  # 点将台
    Break = 33  # 精灵升星
    Giftkey = 34  # CDKEY
    REFINING = 35  # 炼化
    EquipStrengthen = 36  # 装备强化
    EquipAdvance = 37  # 装备进阶
    MineCollect = 38  # 精灵村庄征收
    RefreshRobList = 39  # 精灵村庄刷新抢夺列表
    Rob = 40  # 精灵村庄抢夺
    Uproar = 41  # 训练家之丘
    UproarMall = 42  # 友佳商店
    Loot = 43  # 夺宝
    LootCompose = 44  # 夺宝合成
    LootRefresh = 45  # 夺宝刷新
    LootReset = 46  # 夺宝重置
    Visit = 47  # 梦幻转盘
    LevelPacks = 48  # 冲级礼包
    StarPacks = 49  # 星级奖励
    Compose = 50  # 装备合成
    LimitedPacks = 51  # 限购礼包
    FirstRecharge = 52  # 首充礼包
    TimeLimitedPacks = 53  # 限时礼包
    TriggerPacks1 = 54  # 日冒险礼包
    TriggerPacks2 = 55  # 日多选礼包
    PvpReset = 56  # 重置pvp挑战次数
    PvpRefresh = 57  # 刷新pvp对手
    NpcFight = 58  # 神魔争霸npc
    Spar = 59  # 扭蛋机
    CreatePlayer = 60  # 创建角色
    GiftFriend = 61  # 好友赠送能量
    Tap = 62  # 群魔乱舞奖励
    TreasureRefresh = 63  # 金银山刷新
    Treasure = 64  # 金银山
    Friendfb = 65  # 时之狭间
    TreasureCleanCD = 66  # 金银山清除CD
    FactionLevelReward = 67  # 公会福利
    FactionAlterName = 68  # 公会修改名字
    RefreshMall = 69  # 商店刷新
    MallBuy = 70  # 商店购买
    MallOpen = 71  # 开启商店
    PetPatchExchange = 72  # 碎片
    VipPacks = 73  # 礼包专区、VIP礼包、VIP福利礼包
    AccRechargeReward = 74  # 累计充值
    Wish = 75  # 许愿
    BuyFund = 76  # 购买基金
    CheckInMakeUp = 77  # 补签
    TimedStore = 78  # 限时商店
    FundReward = 79  # 基金奖励
    TriggerStore = 80  # 触发商店
    TriggerChests = 81  # 触发多宝箱
    TriggerChest = 82  # 触发单宝箱
    CreateRole = 83
    MonthlyCard = 84  # 月卡奖励
    EnchantEquip = 85  # 装备洗练
    DlcStarPacks = 86  # Dlc星级
    DlcDispatch = 87  # Dlc派遣奖励
    DlcDoneTask = 88  # Dlc直接完成
    CountDown = 89  # 次日登陆礼包
    FriendfbReborn = 90  # 秘境复活
    GveReborn = 91  # gve 重生
    Fusion = 92  # 合成精灵
    PetSkillUp = 93  # 精灵技能升级
    BuySkillpoint = 94  # 购买技能点
    SwapRefreshCD = 95  # 清除PVPCD
    SwapResetCount = 96  # 重置pvp次数
    SwapFight = 97  # pvp战斗
    MazeDrop = 98  # 迷宫奖励
    MazePool = 99  # 迷宫累计金币领取
    UseMat = 100  # 使用物品
    OnlinePacks = 101  # 在线礼包
    DailyRed = 102  # 红包
    DailyBuyCount = 103  # 每日PVP重置次数
    DailyInspire = 104  # 每日PVP鼓舞
    GuideReward = 105  # 引导奖励
    StrengthenEquip = 106  # 强化装备
    AmbitionUp = 107  # 野望
    GuideDefeat = 108  # 首败奖励
    DailyRechargeReward = 109  # 每日单笔
    SceneRewards = 110  # 场景奖励
    BuySoul = 111  # 购买水晶
    DailyPVP = 112  # 每日PVP奖励
    DailyPVPReborn = 113  # 每日PVP复活
    PetExchange = 114  # 精灵兑换
    MatExchange = 115  # 道具兑换
    CityDungeon = 116  # 黄金城推图
    CityContend = 117  # 黄金城抢夺
    CityContendAttack = 118  # 黄金城争夺抢夺
    CityContendDefend = 119  # 黄金城争夺防守
    CityTreasure = 120  # 黄金城领取宝藏
    Monthcard = 121  # 月卡
    PlayerEquipStrengthen = 122  # 人物装备强化
    ConsumeCampaign = 123  # 累计消耗活动
    LoginCampaign = 124  # 累计登录活动
    PowerPacks = 125  # 巅峰战力奖励
    ExchageCampaign = 126   # 精灵置换活动
    RefreshStoreCampaign = 127   # 刷新商店活动
    ArborDayYYYCampaign = 128   # 植树节遥一摇活动
    SeedCropCampaign = 129   # 种植种子
    SeedReapCampaign = 130   # 种植收割
    SeedCleanCampaign = 131   # 种植清理
    SeedWaterWormCampaign = 132   # 每日浇水和除虫次数用完后
    Flower315Campaign = 133   # 315 BOSS
    ClimbTower = 134  # 爬塔
    GemCompose = 135  # 宝石合成
    GemRefine = 136  # 宝石镶嵌


class RewardItemType:
    Droppack = 0  # 掉落包
    EXP = 1  # 人物经验
    Gold = 2  # 钻石
    Pet = 3  # 石像
    Slate = 4  # 石板
    GP = 5  # GP
    BP = 6  # BP
    VS = 7  # VS
    Money = 8  # 钱币
    SpProp = 9  # 能量道具
    PetMax = 10  # 最大怪物数（怪物格子）
    SP = 11  # 能量
    Patch = 12  # 碎片
    Cleanfb = 13  # 扫荡券
    Mat = 14  # 物品
    FP = 15  # 公会声望
    Soul = 16  # 水晶
    Equip = 17  # 装备
    Jiutian = 18  # 九天
    Specpack = 19  # 特定掉落
    Totalfp = 20  # 公会贡献
    Stone = 21  # 熔石
    Pious = 22  # 虔诚
    Point = 23  # 成就
    Skillpoint = 24  # 技能点
    Ball = 25  # 精灵球
    Refinery = 26  # 分解币
    Dream = 27  # 梦幻转盘抽奖券
    Shopping = 28  # 商店刷新令
    Credits = 29  # VIP 积分
    Phantom = 30  # 幻影币
    Gem = 31  # 宝石

RewardItemTypeDict = {
    k.lower(): v for k,
    v in RewardItemType.__dict__.items() if not k.startswith('__')}
AntiRewardItemTypeDict = {
    v: k.lower() for k,
    v in RewardItemType.__dict__.items() if not k.startswith('__')}


class RandomType:
    Weight = 1
    Independent = 2
