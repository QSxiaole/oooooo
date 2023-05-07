keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        # 向右
        self.pos.x += 5 # ------------------------简单的改变位置
    elif keys[pygame.K_LEFT]:
        # 向左
       if self.vel.x < 0:
            # 这里很细节的加入了一个转向的速度控制
            self.acc.x = -TURNAROUND
            if self.vel.x >= 0:  # ------------------------改变加速度来改变运动
                self.acc.x = -ACC
        # 这里加入了一个最大速度限制
    if abs(self.vel.x) < MAX_SPEED:
        self.vel.x += self.acc.x
    elif keys[pygame.K_LEFT]:
        self.vel.x = -MAX_SPEED
    elif keys[pygame.K_RIGHT]:
        self.vel.x = MAX_SPEED
    # 这里对加速度和速度进行计算得出位移并在下一帧时改变Mario的位置
    self.acc.x += self.vel.x * FRICTION
    # 同时还要引用一个 摩擦力 的概念，随着速度的增大而增大
    self.vel += self.acc
    self.pos += self.vel + 0.5 * self.acc
    self.rect.midbottom = self.pos
    

搜索

打开App

超级玛丽的 python 实现

超级玛丽的 python 实现

3 年前

家里蹲大学落榜生

家里蹲大学落榜生

关注

超级玛丽的 python 实现

在经过三四天的摸索，参考了Github上的一个大神的代码的前提下，也算是初步搭建起了自己的超级玛丽，下面就给大家分享一些自己踩的坑。

这里是Github上大神的代码，对超级玛丽的第一关进行了很好的还原。

推荐一下Github上一个pyga
# 屏幕创建和初始化参数 

self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

self.rect = self.screen.get_rect()

pygame.display.set_caption(TITLE)

# 加载关卡图片

self.background = load_image('level.png')

self.back_rect = self.background.get_rect()

    # 这里载入图片需要乘上特定的系数来适配屏幕的尺寸

self.background = pygame.transform.scale(self.background,

                                     (int(self.back_rect.width * BACKGROUND_SIZE),

                                      int(self.back_rect.height * BACKGROUND_SIZE))).convert()

# 导入Mario

self.sheet = load_image('mario.png')

    # 这里由于Mario会有奔跑和跳跃的速度，所以需要导入一整张图片再裁剪使用。

self.load_from_sheet()

    # 初始化角色的一些基本常量

self.rect = self.image.get_rect()

self.pos = vec(WIDTH * 0.5, GROUND_HEIGHT - 70)

self.vel = vec(0, 0)

self.acc = vec(0, 0)

2. 角色的落地、跳跃和移动

在这之前要解决一下Mario如何才能站在我们定义的地面上

self.acc = vec(0, GRAVITY)

if GROUND_HEIGHT < self.mario.pos.y:

    # 如果Mario低于我们定义的地面，就之间将他的所有速度加速度都置零，之间放在我们的地面上

    # 如果速度和加速度不值零，可能会出现Mario卡在地面上抖动的情况，由于y值的不断变化

    self.mario.acc.y = 0

    self.mario.vel.y = 0

    self.mario.pos.y = self.ground_collide.rect.top

 self.mario.landing = True

正如之前那一篇文章所说，角色的移动如果只是单纯的实现以像素为单位向左向右移动，无疑会很影响玩家的游戏体验正如以下

动图封面

可以明显感觉到两个方向的运动的不同体验，下面是两个方向的代码作为比对

keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:

        # 向右

        self.pos.x += 5 # ------------------------简单的改变位置

    elif keys[pygame.K_LEFT]:

        # 向左

       if self.vel.x < 0:

            # 这里很细节的加入了一个转向的速度控制

            self.acc.x = -TURNAROUND

            if self.vel.x >= 0:  # ------------------------改变加速度来改变运动

                self.acc.x = -ACC

        # 这里加入了一个最大速度限制

    if abs(self.vel.x) < MAX_SPEED:

        self.vel.x += self.acc.x

    elif keys[pygame.K_LEFT]:

        self.vel.x = -MAX_SPEED

    elif keys[pygame.K_RIGHT]:

        self.vel.x = MAX_SPEED

    # 这里对加速度和速度进行计算得出位移并在下一帧时改变Mario的位置

    self.acc.x += self.vel.x * FRICTION

    # 同时还要引用一个 摩擦力 的概念，随着速度的增大而增大

    self.vel += self.acc

    self.pos += self.vel + 0.5 * self.acc

    self.rect.midbottom = self.pos
