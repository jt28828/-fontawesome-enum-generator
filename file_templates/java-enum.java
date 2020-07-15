public enum FontAwesomeCodes {
<<Contents>>

    private final int code;

    FontAwesomeCodes(int code) {
        this.code = code;
    }

    String getCode() {
        return Integer.toHexString(this.code);
    }
}

