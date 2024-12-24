from smpte import Project, Framerate, Cue


project = Project(name="Outlander", code="TOTT", framerate=Framerate.TV)

cue_1m01 = Cue(number="1m01", name="The First Cue", start="01:00:00:00", end="01:01:00:00")
cue_1m02 = Cue(number="1m02", name="The Second Cue", start=cue_1m01.end, end="01:02:01:00")

project.register_cue(cue_1m01)
project.register_cue(cue_1m02)

cue_1m01.get_duration()
