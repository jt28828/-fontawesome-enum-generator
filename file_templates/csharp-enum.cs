/// <summary>
/// Provides a basic method to the enum for converting into back an escaped unicode format so it can be used in a UI
/// </summary>
public static class FontAwesomeCodesExtensions
{
    public static string ToEscapedString(this FontAwesomeCodes code)
    {
        return ((char) code).ToString();
    }
}

public enum FontAwesomeCodes
{
<<Contents>>}
