class PingPong:
  def __init__(self, ping, pong):
    self.ping = ping
    self.pong = pong

  def __repr__(self):
    return f"ping: {self.ping}, pong: {self.pong}"

class PromptFmt:
  @classmethod
  def ctx(cls, context):
    pass

  @classmethod
  def prompt(cls, pingpong):
    pass

class UIFmt:
  @classmethod
  def ui(cls, pingpong):
    pass

class PPManager:
  def __init__(self, ctx: str=""):
    self.ctx = ctx
    self.pingpongs = []

  def add_ping(self, ping, fmt: PromptFmt):
    if len(self.pingpongs) == 0 \
      or (len(self.pingpongs) >= 1 and self.pingpongs[-1].pong is not None):
      self.pingpongs.append(PingPong(ping, None))
      return True
    return False

  def add_pong(self, pong):
    self.replace_last_pong(pong)

  def replace_last_pong(self, pong):
    self.pingpongs[-1].pong = pong

  def append_pong(self, piece_pong):
    self.pingpongs[-1].pong += piece_pong

  def add_pingpong(self, pingpong):
    self.pingpongs.append(pingpong)

  def pop_pingpong(self):
    return self.pingpongs.pop()

  def build_prompts(self, from_idx: int, to_idx: int, fmt: PromptFmt):
    pass

  def build_uis(self, from_idx: int, to_idx: int, fmt: UIFmt):
    pass
    