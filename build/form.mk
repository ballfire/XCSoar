# Build rules for the portable screen library

FORM_SRC_DIR = $(SRC)/Form

FORM_SOURCES = \
	$(FORM_SRC_DIR)/Control.cpp \
	$(FORM_SRC_DIR)/Container.cpp \
	$(FORM_SRC_DIR)/Panel.cpp \
	$(FORM_SRC_DIR)/Form.cpp \
	$(FORM_SRC_DIR)/Button.cpp \
	$(FORM_SRC_DIR)/EventButton.cpp \
	$(FORM_SRC_DIR)/Frame.cpp \
	$(FORM_SRC_DIR)/Draw.cpp \
	$(FORM_SRC_DIR)/List.cpp \
	$(FORM_SRC_DIR)/ScrollBar.cpp \
	$(FORM_SRC_DIR)/Edit.cpp \
	$(FORM_SRC_DIR)/Tabbed.cpp \
	$(FORM_SRC_DIR)/Util.cpp

FORM_LIBS = $(TARGET_OUTPUT_DIR)/form.a

$(FORM_LIBS): $(call SRC_TO_OBJ,$(FORM_SOURCES))
	@$(NQ)echo "  AR      $@"
	$(Q)$(AR) $(ARFLAGS) $@ $^
