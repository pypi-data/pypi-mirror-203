# asimtote.ios.converters.other
#
# Copyright (C) Robert Franklin <rcf34@cam.ac.uk>



# --- imports ---



from ...diff import DiffConvert



# --- converter classes ---



# =============================================================================
# hostname ...
# =============================================================================



class Cvt_Hostname(DiffConvert):
    cmd = "hostname",

    def remove(self, old, c):
        return "no hostname"

    def update(self, old, upd, new, c):
        return "hostname " + new



# =============================================================================
# [no] spanning-tree ...
# =============================================================================



class Cvt_NoSTP(DiffConvert):
    cmd = "no-spanning-tree-vlan", None

    def remove(self, old, c, tag):
        # removing 'no spanning-tree' enables spanning-tree
        return "spanning-tree vlan %d" % tag

    def update(self, old, upd, new, c, tag):
        # adding 'no spanning-tree' disables spanning-tree
        return "no spanning-tree vlan %d" % tag


class Cvt_STPPri(DiffConvert):
    cmd = "spanning-tree-vlan-priority", None

    def remove(self, old, c, tag):
        return "no spanning-tree vlan %d priority" % tag

    def update(self, old, upd, new, c, tag):
        return "spanning-tree vlan %d priority %d" % (tag, new)



# =============================================================================
# track ...
# =============================================================================



# the track command is odd in that it doesn't allow the type of tracking
# object to be changed (e.g. from an interface to a route) and must be
# destroyed and created anew
#
# the parameters of the type of track can, however, be changed, e.g. the
# specific interface or route that's being tracked



class Cvt_Track(DiffConvert):
    cmd = "track", None

    def remove(self, old, c, obj_num):
        return "no track %d" % obj_num


class Cvt_TrackUpdate(DiffConvert):
    cmd = "track", None
    ext = "type",

    # when the type of a tracking object is changed, it must be deleted
    # and the new type created - this does not need to happen when a new
    # one is added, though

    def add(self, new, c, obj_num):
        pass

    def update(self, old, upd, new, c, obj_num):
        return "no track " + str(obj_num)


class DiffConvert_TrackCreate(DiffConvert):
    context = "track", None
    block = "track-create"
    trigger_blocks = { "track-sub" }


class Cvt_TrackInterface(DiffConvert_TrackCreate):
    cmd = "interface",

    def update(self, old, upd, new, c):
        obj_num, = c
        return ["track %d interface %s %s"
                    % (obj_num, new["interface"], new["capability"])]


class Cvt_TrackList(DiffConvert_TrackCreate):
    cmd = "list",

    def update(self, old, upd, new, c):
        obj_num, = c
        if new["type"] == "boolean":
            return ["track %d list boolean %s" % (obj_num, new["op"])]

        return ValueError("unhandled track list type:" + l["type"])


class Cvt_TrackRoute(DiffConvert_TrackCreate):
    cmd = "route",

    def update(self, old, upd, new, c):
        obj_num, = c
        return ["track %d %s route %s %s"
                    % (obj_num, new["proto"], new["net"], new["measure"])]


class DiffConvert_TrackSub(DiffConvert):
    context = Cvt_Track.cmd
    block = "track-sub"

    def enter(self, obj_num):
        return ["track %d" % obj_num]


class Cvt_Track_Delay(DiffConvert_TrackSub):
    cmd = "delay",

    def truncate(self, old, rem, new, c):
        # delays cannot individually be removed from a tracking object;
        # only all delays at the same time
        #
        # to remove a delay, we have to clear them all and re-add the
        # one we're keeping
        #
        # we only re-add it here, though, if new value is the same as
        # the old, otherwise we handle the change separately in update()
        c = self.enter(*c) + [" no delay"]
        for dir_ in sorted(new or []):
            if (dir_ in (old or [])) and (old[dir_] == new[dir_]):
                c.append(" delay %s %d" % (dir_, new[dir_]))
        return c

    def update(self, old, upd, new, c):
        c = self.enter(*c)
        for dir_ in sorted(upd):
            c.append(" delay %s %d" % (dir_, new[dir_]))
        return c


class Cvt_Track_IPVRF(DiffConvert_TrackSub):
    cmd = "ip-vrf",

    def remove(self, old, c):
        return self.enter(*c) + [" no ip vrf"]

    def update(self, old, upd, new, c):
        return self.enter(*c) + [" ip vrf " + new]


class Cvt_Track_IPv6VRF(DiffConvert_TrackSub):
    cmd = "ipv6-vrf",

    def remove(self, old, c):
        return self.enter(*c) + [" no ipv6 vrf"]

    def update(self, old, upd, new, c):
        return self.enter(*c) + [" ipv6 vrf " + new]


class Cvt_Track_ListObj(DiffConvert_TrackSub):
    cmd = "object", None

    def remove(self, old, c, sub_obj_num):
        return self.enter(*c) + [" no object " + str(sub_obj_num)]

    def update(self, old, upd, new, c, sub_obj_num):
        return self.enter(*c) + [" object " + str(sub_obj_num)]



# =============================================================================
# vlan ...
# =============================================================================



class Cvt_VLAN(DiffConvert):
    cmd = "vlan", None

    def remove(self, old, c, tag):
        return "no vlan %d" % tag

    def add(self, new, c, tag):
        return "vlan %d" % tag


class DiffConvert_VLAN(DiffConvert):
    def enter(self, tag):
        return ["vlan %d" % tag]


class Cvt_VLAN_Name(DiffConvert_VLAN):
    context = Cvt_VLAN.cmd
    cmd = "name",

    def remove(self, old, c):
        return self.enter(*c) + [" no name"]

    def update(self, old, upd, new, c):
        return self.enter(*c) + [" name " + new]



# =============================================================================
# vrf definition ...
# =============================================================================



class Cvt_VRF(DiffConvert):
    cmd = "vrf", None

    def remove(self, old, c, name):
        return "no vrf definition " + name

    def add(self, new,  c, name):
        return "vrf definition " + name


class DiffConvert_VRF(DiffConvert):
    context = Cvt_VRF.cmd

    def enter(self, vrf_name):
        return ["vrf definition " + vrf_name]


class Cvt_VRF_RD(DiffConvert_VRF):
    cmd = "rd",

    def remove(self, old, c):
        return self.enter(*c) + [" no rd " + old]

    def update(self, old, upd, new, c):
        l = list(super().enter(*c))
        if old:
            l.append(" no rd " + old)
        l.append(" rd " + new)
        return l


class Cvt_VRF_RT(DiffConvert_VRF):
    cmd = "route-target", None, None

    def truncate(self, old, rem, new, c, dir_, rt):
        return self.enter(*c) + [" no route-target %s %s" % (dir_, rt)]

    def update(self, old, upd, new, c, dir_, rt):
        return self.enter(*c) + [" route-target %s %s" % (dir_, rt)]


class Cvt_VRF_AF(DiffConvert_VRF):
    cmd = "address-family", None

    def remove(self, old, c, af):
        return self.enter(*c) + [" no address-family " + af]

    def add(self, new, c, af):
        return self.enter(*c) + [" address-family " + af]


class DiffConvert_VRF_AF(DiffConvert_VRF):
    context = DiffConvert_VRF.context + Cvt_VRF_AF.cmd

    def enter(self, vrf_name, af):
        return [*super().enter(vrf_name), " address-family " + af]


class Cvt_VRF_AF_RT(DiffConvert_VRF_AF):
    cmd = "route-target", None, None

    def truncate(self, old, rem, new, c, dir_, rt):
        return self.enter(*c) + ["  no route-target %s %s" % (dir_, rt)]

    def update(self, old, upd, new, c, dir_, rt):
        return self.enter(*c) + ["  route-target %s %s" % (dir_, rt)]
