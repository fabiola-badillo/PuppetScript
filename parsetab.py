
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'A Acceleration AltGr Ampersand Asterisk At B BackQuote Backslash Backspace Break C CHARACTERCONTROLLER CapsLock Caret Clear Colon Comma D DASH Dollar DoubleQuote E EQUALS Equals Escape Exclaim F Float Force G Gravity Greater H Hash Help Horizontal I ID Impulse J JETPACK JUMP K L LeftAlt LeftBracket LeftCommand LeftControl LeftParen LeftShift LeftWindows Less M Minus N NONE O P Pause Period Plus Print Q Question Quote R RIGIDBODY Return RightAlt RightApple RightBracket RightCommand RightControl RightParen RightShift RightWindows S SIMPLE ScrollLock Semicolon Slash Space Speed SysReq T Tab U Underscore V Vertical W WALK X Y Zscript : Simple\n                | RigidBody\n                | CharacterControllerSimple : SIMPLE SpeedId MovementRigidBody : RIGIDBODY SpeedId  Movement  ForceMode  ActionCharacterController : CHARACTERCONTROLLER SpeedId GravityId Movement  ActionSpeedId : Speed EQUALS FloatGravityId : Gravity EQUALS FloatMovement : ID EQUALS Direction ID EQUALS Direction  ID EQUALS DirectionDirection : Horizontal\n    | NONE\n    | VerticalForceMode : Force\n                 | Impulse\n                 | Acceleration\n                 | NONEAction : Jump\n                  | Dash\n                  | JetPack\n                  | WalkKeyCode : \n          | A\n          | B\n          | C\n          | D\n          | E\n          | F\n          | G\n          | H\n          | I\n          | J\n          | K\n          | L\n          | M\n          | N\n          | O\n          | P\n          | Q\n          | R\n          | S\n          | T\n          | U\n          | V\n          | W\n          | X\n          | Y\n          | Z\n          | Backspace\n          | Tab\n          | SysReq\n          | Break\n          | CapsLock\n          | ScrollLock\n          | RightShift\n          | LeftShift\n          | RightControl\n          | LeftControl\n          | RightAlt\n          | LeftAlt\n          | RightCommand\n          | RightApple\n          | LeftCommand\n          | LeftWindows\n          | RightWindows\n          | AltGr\n          | Help\n          | Print\n          | Clear\n          | Return\n          | Pause\n          | Escape\n          | Space\n          | Exclaim\n          | DoubleQuote\n          | Hash\n          | Dollar\n\t\t  | Ampersand\n\t\t  | Quote\n\t\t  | LeftParen\n\t\t  | RightParen\n\t\t  | Asterisk\n\t\t  | Plus\n\t\t  | Comma\n\t\t  | Minus\n\t\t  | Period\n\t\t  | Slash\n\t\t  | Colon\n\t\t  | Semicolon\n\t\t  | Less\n\t\t  | Equals\n\t\t  | Greater\n\t\t  | Question\n\t\t  | At\n\t\t  | LeftBracket\n\t\t  | Backslash\n\t\t  | RightBracket\n\t\t  | Caret\n\t\t  | Underscore\n\t\t  | BackQuote\n\t\t  \nJump : JUMP EQUALS KeyCode\n            | JUMP EQUALS KeyCode ActionDash : DASH EQUALS KeyCode\n            | DASH EQUALS KeyCode ActionWalk : WALK EQUALS KeyCode\n            | WALK EQUALS KeyCode ActionJetPack : JETPACK EQUALS KeyCode\n            | JETPACK EQUALS KeyCode Action'
    
_lr_action_items = {'SIMPLE':([0,],[5,]),'RIGIDBODY':([0,],[6,]),'CHARACTERCONTROLLER':([0,],[7,]),'$end':([1,2,3,4,12,28,29,30,31,32,33,34,35,40,43,44,45,46,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,131,132,133,134,137,],[0,-1,-2,-3,-4,-10,-11,-12,-5,-17,-18,-19,-20,-6,-21,-21,-21,-21,-100,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,-89,-90,-91,-92,-93,-94,-95,-96,-97,-98,-99,-102,-106,-104,-101,-103,-107,-105,-9,]),'Speed':([5,6,7,],[9,9,9,]),'ID':([8,10,16,19,27,28,29,30,41,130,],[13,13,13,-7,42,-10,-11,-12,-8,135,]),'EQUALS':([9,13,17,36,37,38,39,42,135,],[14,18,26,43,44,45,46,47,136,]),'Gravity':([11,19,],[17,-7,]),'Float':([14,26,],[19,41,]),'Force':([15,28,29,30,137,],[21,-10,-11,-12,-9,]),'Impulse':([15,28,29,30,137,],[22,-10,-11,-12,-9,]),'Acceleration':([15,28,29,30,137,],[23,-10,-11,-12,-9,]),'NONE':([15,18,28,29,30,47,136,137,],[24,29,-10,-11,-12,29,29,-9,]),'Horizontal':([18,47,136,],[28,28,28,]),'Vertical':([18,47,136,],[30,30,30,]),'JUMP':([20,21,22,23,24,25,28,29,30,43,44,45,46,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,137,],[36,-13,-14,-15,-16,36,-10,-11,-12,-21,-21,-21,-21,36,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,-89,-90,-91,-92,-93,-94,-95,-96,-97,-98,-99,36,36,36,-9,]),'DASH':([20,21,22,23,24,25,28,29,30,43,44,45,46,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,137,],[37,-13,-14,-15,-16,37,-10,-11,-12,-21,-21,-21,-21,37,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,-89,-90,-91,-92,-93,-94,-95,-96,-97,-98,-99,37,37,37,-9,]),'JETPACK':([20,21,22,23,24,25,28,29,30,43,44,45,46,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,137,],[38,-13,-14,-15,-16,38,-10,-11,-12,-21,-21,-21,-21,38,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,-89,-90,-91,-92,-93,-94,-95,-96,-97,-98,-99,38,38,38,-9,]),'WALK':([20,21,22,23,24,25,28,29,30,43,44,45,46,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,137,],[39,-13,-14,-15,-16,39,-10,-11,-12,-21,-21,-21,-21,39,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,-89,-90,-91,-92,-93,-94,-95,-96,-97,-98,-99,39,39,39,-9,]),'A':([43,44,45,46,],[49,49,49,49,]),'B':([43,44,45,46,],[50,50,50,50,]),'C':([43,44,45,46,],[51,51,51,51,]),'D':([43,44,45,46,],[52,52,52,52,]),'E':([43,44,45,46,],[53,53,53,53,]),'F':([43,44,45,46,],[54,54,54,54,]),'G':([43,44,45,46,],[55,55,55,55,]),'H':([43,44,45,46,],[56,56,56,56,]),'I':([43,44,45,46,],[57,57,57,57,]),'J':([43,44,45,46,],[58,58,58,58,]),'K':([43,44,45,46,],[59,59,59,59,]),'L':([43,44,45,46,],[60,60,60,60,]),'M':([43,44,45,46,],[61,61,61,61,]),'N':([43,44,45,46,],[62,62,62,62,]),'O':([43,44,45,46,],[63,63,63,63,]),'P':([43,44,45,46,],[64,64,64,64,]),'Q':([43,44,45,46,],[65,65,65,65,]),'R':([43,44,45,46,],[66,66,66,66,]),'S':([43,44,45,46,],[67,67,67,67,]),'T':([43,44,45,46,],[68,68,68,68,]),'U':([43,44,45,46,],[69,69,69,69,]),'V':([43,44,45,46,],[70,70,70,70,]),'W':([43,44,45,46,],[71,71,71,71,]),'X':([43,44,45,46,],[72,72,72,72,]),'Y':([43,44,45,46,],[73,73,73,73,]),'Z':([43,44,45,46,],[74,74,74,74,]),'Backspace':([43,44,45,46,],[75,75,75,75,]),'Tab':([43,44,45,46,],[76,76,76,76,]),'SysReq':([43,44,45,46,],[77,77,77,77,]),'Break':([43,44,45,46,],[78,78,78,78,]),'CapsLock':([43,44,45,46,],[79,79,79,79,]),'ScrollLock':([43,44,45,46,],[80,80,80,80,]),'RightShift':([43,44,45,46,],[81,81,81,81,]),'LeftShift':([43,44,45,46,],[82,82,82,82,]),'RightControl':([43,44,45,46,],[83,83,83,83,]),'LeftControl':([43,44,45,46,],[84,84,84,84,]),'RightAlt':([43,44,45,46,],[85,85,85,85,]),'LeftAlt':([43,44,45,46,],[86,86,86,86,]),'RightCommand':([43,44,45,46,],[87,87,87,87,]),'RightApple':([43,44,45,46,],[88,88,88,88,]),'LeftCommand':([43,44,45,46,],[89,89,89,89,]),'LeftWindows':([43,44,45,46,],[90,90,90,90,]),'RightWindows':([43,44,45,46,],[91,91,91,91,]),'AltGr':([43,44,45,46,],[92,92,92,92,]),'Help':([43,44,45,46,],[93,93,93,93,]),'Print':([43,44,45,46,],[94,94,94,94,]),'Clear':([43,44,45,46,],[95,95,95,95,]),'Return':([43,44,45,46,],[96,96,96,96,]),'Pause':([43,44,45,46,],[97,97,97,97,]),'Escape':([43,44,45,46,],[98,98,98,98,]),'Space':([43,44,45,46,],[99,99,99,99,]),'Exclaim':([43,44,45,46,],[100,100,100,100,]),'DoubleQuote':([43,44,45,46,],[101,101,101,101,]),'Hash':([43,44,45,46,],[102,102,102,102,]),'Dollar':([43,44,45,46,],[103,103,103,103,]),'Ampersand':([43,44,45,46,],[104,104,104,104,]),'Quote':([43,44,45,46,],[105,105,105,105,]),'LeftParen':([43,44,45,46,],[106,106,106,106,]),'RightParen':([43,44,45,46,],[107,107,107,107,]),'Asterisk':([43,44,45,46,],[108,108,108,108,]),'Plus':([43,44,45,46,],[109,109,109,109,]),'Comma':([43,44,45,46,],[110,110,110,110,]),'Minus':([43,44,45,46,],[111,111,111,111,]),'Period':([43,44,45,46,],[112,112,112,112,]),'Slash':([43,44,45,46,],[113,113,113,113,]),'Colon':([43,44,45,46,],[114,114,114,114,]),'Semicolon':([43,44,45,46,],[115,115,115,115,]),'Less':([43,44,45,46,],[116,116,116,116,]),'Equals':([43,44,45,46,],[117,117,117,117,]),'Greater':([43,44,45,46,],[118,118,118,118,]),'Question':([43,44,45,46,],[119,119,119,119,]),'At':([43,44,45,46,],[120,120,120,120,]),'LeftBracket':([43,44,45,46,],[121,121,121,121,]),'Backslash':([43,44,45,46,],[122,122,122,122,]),'RightBracket':([43,44,45,46,],[123,123,123,123,]),'Caret':([43,44,45,46,],[124,124,124,124,]),'Underscore':([43,44,45,46,],[125,125,125,125,]),'BackQuote':([43,44,45,46,],[126,126,126,126,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'script':([0,],[1,]),'Simple':([0,],[2,]),'RigidBody':([0,],[3,]),'CharacterController':([0,],[4,]),'SpeedId':([5,6,7,],[8,10,11,]),'Movement':([8,10,16,],[12,15,25,]),'GravityId':([11,],[16,]),'ForceMode':([15,],[20,]),'Direction':([18,47,136,],[27,130,137,]),'Action':([20,25,48,127,128,129,],[31,40,131,132,133,134,]),'Jump':([20,25,48,127,128,129,],[32,32,32,32,32,32,]),'Dash':([20,25,48,127,128,129,],[33,33,33,33,33,33,]),'JetPack':([20,25,48,127,128,129,],[34,34,34,34,34,34,]),'Walk':([20,25,48,127,128,129,],[35,35,35,35,35,35,]),'KeyCode':([43,44,45,46,],[48,127,128,129,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> script","S'",1,None,None,None),
  ('script -> Simple','script',1,'p_script_type','CodeParser.py',18),
  ('script -> RigidBody','script',1,'p_script_type','CodeParser.py',19),
  ('script -> CharacterController','script',1,'p_script_type','CodeParser.py',20),
  ('Simple -> SIMPLE SpeedId Movement','Simple',3,'p_simple_script','CodeParser.py',23),
  ('RigidBody -> RIGIDBODY SpeedId Movement ForceMode Action','RigidBody',5,'p_rigid_script','CodeParser.py',36),
  ('CharacterController -> CHARACTERCONTROLLER SpeedId GravityId Movement Action','CharacterController',5,'p_chraracter_controller_script','CodeParser.py',55),
  ('SpeedId -> Speed EQUALS Float','SpeedId',3,'p_speed_Id','CodeParser.py',73),
  ('GravityId -> Gravity EQUALS Float','GravityId',3,'p_gravity_Id','CodeParser.py',81),
  ('Movement -> ID EQUALS Direction ID EQUALS Direction ID EQUALS Direction','Movement',9,'p_movement_rule','CodeParser.py',87),
  ('Direction -> Horizontal','Direction',1,'p_Direction','CodeParser.py',99),
  ('Direction -> NONE','Direction',1,'p_Direction','CodeParser.py',100),
  ('Direction -> Vertical','Direction',1,'p_Direction','CodeParser.py',101),
  ('ForceMode -> Force','ForceMode',1,'p_force_mode','CodeParser.py',106),
  ('ForceMode -> Impulse','ForceMode',1,'p_force_mode','CodeParser.py',107),
  ('ForceMode -> Acceleration','ForceMode',1,'p_force_mode','CodeParser.py',108),
  ('ForceMode -> NONE','ForceMode',1,'p_force_mode','CodeParser.py',109),
  ('Action -> Jump','Action',1,'p_action','CodeParser.py',114),
  ('Action -> Dash','Action',1,'p_action','CodeParser.py',115),
  ('Action -> JetPack','Action',1,'p_action','CodeParser.py',116),
  ('Action -> Walk','Action',1,'p_action','CodeParser.py',117),
  ('KeyCode -> <empty>','KeyCode',0,'p_KeyCode','CodeParser.py',127),
  ('KeyCode -> A','KeyCode',1,'p_KeyCode','CodeParser.py',128),
  ('KeyCode -> B','KeyCode',1,'p_KeyCode','CodeParser.py',129),
  ('KeyCode -> C','KeyCode',1,'p_KeyCode','CodeParser.py',130),
  ('KeyCode -> D','KeyCode',1,'p_KeyCode','CodeParser.py',131),
  ('KeyCode -> E','KeyCode',1,'p_KeyCode','CodeParser.py',132),
  ('KeyCode -> F','KeyCode',1,'p_KeyCode','CodeParser.py',133),
  ('KeyCode -> G','KeyCode',1,'p_KeyCode','CodeParser.py',134),
  ('KeyCode -> H','KeyCode',1,'p_KeyCode','CodeParser.py',135),
  ('KeyCode -> I','KeyCode',1,'p_KeyCode','CodeParser.py',136),
  ('KeyCode -> J','KeyCode',1,'p_KeyCode','CodeParser.py',137),
  ('KeyCode -> K','KeyCode',1,'p_KeyCode','CodeParser.py',138),
  ('KeyCode -> L','KeyCode',1,'p_KeyCode','CodeParser.py',139),
  ('KeyCode -> M','KeyCode',1,'p_KeyCode','CodeParser.py',140),
  ('KeyCode -> N','KeyCode',1,'p_KeyCode','CodeParser.py',141),
  ('KeyCode -> O','KeyCode',1,'p_KeyCode','CodeParser.py',142),
  ('KeyCode -> P','KeyCode',1,'p_KeyCode','CodeParser.py',143),
  ('KeyCode -> Q','KeyCode',1,'p_KeyCode','CodeParser.py',144),
  ('KeyCode -> R','KeyCode',1,'p_KeyCode','CodeParser.py',145),
  ('KeyCode -> S','KeyCode',1,'p_KeyCode','CodeParser.py',146),
  ('KeyCode -> T','KeyCode',1,'p_KeyCode','CodeParser.py',147),
  ('KeyCode -> U','KeyCode',1,'p_KeyCode','CodeParser.py',148),
  ('KeyCode -> V','KeyCode',1,'p_KeyCode','CodeParser.py',149),
  ('KeyCode -> W','KeyCode',1,'p_KeyCode','CodeParser.py',150),
  ('KeyCode -> X','KeyCode',1,'p_KeyCode','CodeParser.py',151),
  ('KeyCode -> Y','KeyCode',1,'p_KeyCode','CodeParser.py',152),
  ('KeyCode -> Z','KeyCode',1,'p_KeyCode','CodeParser.py',153),
  ('KeyCode -> Backspace','KeyCode',1,'p_KeyCode','CodeParser.py',154),
  ('KeyCode -> Tab','KeyCode',1,'p_KeyCode','CodeParser.py',155),
  ('KeyCode -> SysReq','KeyCode',1,'p_KeyCode','CodeParser.py',156),
  ('KeyCode -> Break','KeyCode',1,'p_KeyCode','CodeParser.py',157),
  ('KeyCode -> CapsLock','KeyCode',1,'p_KeyCode','CodeParser.py',158),
  ('KeyCode -> ScrollLock','KeyCode',1,'p_KeyCode','CodeParser.py',159),
  ('KeyCode -> RightShift','KeyCode',1,'p_KeyCode','CodeParser.py',160),
  ('KeyCode -> LeftShift','KeyCode',1,'p_KeyCode','CodeParser.py',161),
  ('KeyCode -> RightControl','KeyCode',1,'p_KeyCode','CodeParser.py',162),
  ('KeyCode -> LeftControl','KeyCode',1,'p_KeyCode','CodeParser.py',163),
  ('KeyCode -> RightAlt','KeyCode',1,'p_KeyCode','CodeParser.py',164),
  ('KeyCode -> LeftAlt','KeyCode',1,'p_KeyCode','CodeParser.py',165),
  ('KeyCode -> RightCommand','KeyCode',1,'p_KeyCode','CodeParser.py',166),
  ('KeyCode -> RightApple','KeyCode',1,'p_KeyCode','CodeParser.py',167),
  ('KeyCode -> LeftCommand','KeyCode',1,'p_KeyCode','CodeParser.py',168),
  ('KeyCode -> LeftWindows','KeyCode',1,'p_KeyCode','CodeParser.py',169),
  ('KeyCode -> RightWindows','KeyCode',1,'p_KeyCode','CodeParser.py',170),
  ('KeyCode -> AltGr','KeyCode',1,'p_KeyCode','CodeParser.py',171),
  ('KeyCode -> Help','KeyCode',1,'p_KeyCode','CodeParser.py',172),
  ('KeyCode -> Print','KeyCode',1,'p_KeyCode','CodeParser.py',173),
  ('KeyCode -> Clear','KeyCode',1,'p_KeyCode','CodeParser.py',174),
  ('KeyCode -> Return','KeyCode',1,'p_KeyCode','CodeParser.py',175),
  ('KeyCode -> Pause','KeyCode',1,'p_KeyCode','CodeParser.py',176),
  ('KeyCode -> Escape','KeyCode',1,'p_KeyCode','CodeParser.py',177),
  ('KeyCode -> Space','KeyCode',1,'p_KeyCode','CodeParser.py',178),
  ('KeyCode -> Exclaim','KeyCode',1,'p_KeyCode','CodeParser.py',179),
  ('KeyCode -> DoubleQuote','KeyCode',1,'p_KeyCode','CodeParser.py',180),
  ('KeyCode -> Hash','KeyCode',1,'p_KeyCode','CodeParser.py',181),
  ('KeyCode -> Dollar','KeyCode',1,'p_KeyCode','CodeParser.py',182),
  ('KeyCode -> Ampersand','KeyCode',1,'p_KeyCode','CodeParser.py',183),
  ('KeyCode -> Quote','KeyCode',1,'p_KeyCode','CodeParser.py',184),
  ('KeyCode -> LeftParen','KeyCode',1,'p_KeyCode','CodeParser.py',185),
  ('KeyCode -> RightParen','KeyCode',1,'p_KeyCode','CodeParser.py',186),
  ('KeyCode -> Asterisk','KeyCode',1,'p_KeyCode','CodeParser.py',187),
  ('KeyCode -> Plus','KeyCode',1,'p_KeyCode','CodeParser.py',188),
  ('KeyCode -> Comma','KeyCode',1,'p_KeyCode','CodeParser.py',189),
  ('KeyCode -> Minus','KeyCode',1,'p_KeyCode','CodeParser.py',190),
  ('KeyCode -> Period','KeyCode',1,'p_KeyCode','CodeParser.py',191),
  ('KeyCode -> Slash','KeyCode',1,'p_KeyCode','CodeParser.py',192),
  ('KeyCode -> Colon','KeyCode',1,'p_KeyCode','CodeParser.py',193),
  ('KeyCode -> Semicolon','KeyCode',1,'p_KeyCode','CodeParser.py',194),
  ('KeyCode -> Less','KeyCode',1,'p_KeyCode','CodeParser.py',195),
  ('KeyCode -> Equals','KeyCode',1,'p_KeyCode','CodeParser.py',196),
  ('KeyCode -> Greater','KeyCode',1,'p_KeyCode','CodeParser.py',197),
  ('KeyCode -> Question','KeyCode',1,'p_KeyCode','CodeParser.py',198),
  ('KeyCode -> At','KeyCode',1,'p_KeyCode','CodeParser.py',199),
  ('KeyCode -> LeftBracket','KeyCode',1,'p_KeyCode','CodeParser.py',200),
  ('KeyCode -> Backslash','KeyCode',1,'p_KeyCode','CodeParser.py',201),
  ('KeyCode -> RightBracket','KeyCode',1,'p_KeyCode','CodeParser.py',202),
  ('KeyCode -> Caret','KeyCode',1,'p_KeyCode','CodeParser.py',203),
  ('KeyCode -> Underscore','KeyCode',1,'p_KeyCode','CodeParser.py',204),
  ('KeyCode -> BackQuote','KeyCode',1,'p_KeyCode','CodeParser.py',205),
  ('Jump -> JUMP EQUALS KeyCode','Jump',3,'p_Jump','CodeParser.py',214),
  ('Jump -> JUMP EQUALS KeyCode Action','Jump',4,'p_Jump','CodeParser.py',215),
  ('Dash -> DASH EQUALS KeyCode','Dash',3,'p_Dash','CodeParser.py',231),
  ('Dash -> DASH EQUALS KeyCode Action','Dash',4,'p_Dash','CodeParser.py',232),
  ('Walk -> WALK EQUALS KeyCode','Walk',3,'p_Walk','CodeParser.py',249),
  ('Walk -> WALK EQUALS KeyCode Action','Walk',4,'p_Walk','CodeParser.py',250),
  ('JetPack -> JETPACK EQUALS KeyCode','JetPack',3,'p_JetPack','CodeParser.py',269),
  ('JetPack -> JETPACK EQUALS KeyCode Action','JetPack',4,'p_JetPack','CodeParser.py',270),
]
